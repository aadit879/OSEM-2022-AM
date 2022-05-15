import geopandas as gpd
import numpy as np
import os
import pandas as pd



def to_hotmaps_csv(x):
    """
    Description: Converts THERMOS outputs into inputs favourable for hotmaps
    
    Inputs
    -------
    x: File path in GEOjson format
    
    Returns
    -------
    area_buildings : pandas.DataFrame
        Buildings with considerably higher demand are filtered out
    """
    area = gpd.read_file(os.path.join(x))
    area_buildings = area[area.connection_count==1]
    area_buildings = area_buildings.to_crs('EPSG:3035')
    area_buildings['centroid']=area_buildings.geometry.centroid
    area_buildings['area']=area_buildings.area
    
    area_buildings['X_3035'] = area_buildings.centroid.map(lambda p:p.x)
    area_buildings.X_3035=area_buildings.X_3035.astype(int)
    area_buildings['Y_3035']=area_buildings.centroid.map(lambda p:p.y)
    area_buildings.Y_3035=area_buildings.Y_3035.astype(int)
    
    area_buildings.drop(columns=area_buildings.columns.difference(
            ['orig_id','area','demand_kwh_per_year','X_3035','Y_3035']),
                        inplace=True)
    area_buildings.insert(1,'hotmaps_ID',np.arange(len(area_buildings))+1)
    area_buildings.insert(2,'construction',0)    
    area_buildings.insert(3,'GFA',area_buildings['area'])
    area_buildings.rename(columns={'orig_id':'ID_shp','demand_kwh_per_year':'demand'},inplace=True)
                                   
    area_buildings = area_buildings[['ID_shp', 'hotmaps_ID', 'construction','GFA','demand',
                                     'X_3035','Y_3035']]
    
    return area_buildings

def identify_demand_outlier(x):
       
    """
    Description: Identify upper extreme values in the dataset
    
    Inputs
    -------
    x: file path in GEOjson format
    
    Returns
    -------
    area_buildings : pandas.DataFrame
        Buildings with considerably higher demand are filtered out
    """
    area_buildings = to_hotmaps_csv(x)
    area_buildings['Specific_Demand']= area_buildings.demand/ area_buildings.GFA
    area_buildings = area_buildings[area_buildings.Specific_Demand > area_buildings.Specific_Demand.quantile(0.8)]
        
    return area_buildings
