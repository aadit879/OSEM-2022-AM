# OSEM-2022-AM
Setting up unit tests

Copyright (c) 2022 Aadit Malla


**Version 1.0.0**

**Description**<br>

* The function utils.to_hotmaps_csv converts the data downloaded from THERMOS database into a format required by the HOTMAPS’ calculation module.
* The function utils. identify_demand_outlier identifies buildings that have extremely high heat demand values.

The results of the functions are used for further analysis in the original codes (not included in this repository).

For the unit tests, the test data in the tests/Data directory, a GEOjson file, is used, which is a sample data downloaded from the THERMOS database.


[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
