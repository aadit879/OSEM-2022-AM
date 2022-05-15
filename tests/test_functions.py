
import os
import sys
path = os.path.dirname(os.path.abspath(__file__))
path_parent = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))


if path_parent not in sys.path:
     sys.path.append(path_parent)

## not the best way to do it
from utils import to_hotmaps_csv
from utils import identify_demand_outlier


def test_to_hotmaps_csv():
    x = os.path.join(path,'Data','San_Sebastian_sample.json')
    output = to_hotmaps_csv(x)
    assert list(output.columns)== ['ID_shp', 'hotmaps_ID', 'construction', 'GFA', 'demand', 'X_3035', 'Y_3035']

def test_identify_demand_outlier():
    x = os.path.join(path,'Data','San_Sebastian_sample.json')
    output = identify_demand_outlier(x)
    assert output.Specific_Demand.mean() < 85