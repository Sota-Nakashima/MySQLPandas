MySQLPandas
============
[![pages-build-deployment](https://github.com/Sota-Nakashima/MySQLPandas/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/Sota-Nakashima/MySQLPandas/actions/workflows/pages/pages-build-deployment)
[![Version](https://img.shields.io/badge/stable-main-gree)](https://github.com/Sota-Nakashima/MySQLPandas)
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/Sota-Nakashima/MySQLPandas/blob/main/LICENCE)
#  Overview
Simple connector between MySQL(MariaDB) and Pandas

## Description
This tool is primarily intended to help Python users easily handle databases.
It uses Pandas as its base, so it should be easy to use even for those who are not familiar with databases.
The tool supports MySQL or MariaDB as the database engine.
## Demo
* Make new table and install dataframe or csv
```python:tutoring.py
from MySQLPandas.core import MySQLPandas
with MySQLPandas("hoge","hoge_db",initfile_path="hoge.ini") as obj:
    obj.makeTable("sample_table",df_path="sample.csv")
    obj.showTableinfo("sample_table")
    obj.insertRecord("sample_table",df_path="sample.csv")
```

About other functions, see [here](https://sota-nakashima.github.io/MySQLPandas/MySQLPandas.html).
## Requirement
* MySQL(MariaDB)  
The version of Auther's MariaDB is 5.5.68-MariaDB MariaDB Server.  
Don't try the newest version so please check your MariaDB version.
* Pandas <= 1.5.3
* Python 3.*
* mysql-connector-python <= 8.0.29

## Pages
See [here](https://sota-nakashima.github.io/MySQLPandas/).
## Install
Install through pip.
```
pip install MySQLPandas
```

## Licence

[MIT](https://github.com/Sota-Nakashima/SSERAFIM/blob/main/LICENCE)

## Author

[Sota Nakashima](https://github.com/Sota-Nakashima)
