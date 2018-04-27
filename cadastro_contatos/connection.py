import pypyodbc
import mysql.connector
#import pymysql
"""from __future__ import print_function
import cx_Oracle"""

class Connection():
    def conecta_msql(self):
        conn = pypyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=server_name;'
            'DATABASE=teste;'
            'UID=user;'
            'PWD=xxxxx$'
            )
        return conn

    def conecta_mysql(self):
        config = {
            'user': 'root',
            'password': '',
            'host': '127.0.0.1',
            'database': 'test',
            'port': 3306,
            'raise_on_warnings': True,
        }
        conn2 = mysql.connector.connect(**config)
        return conn2
    
    def conecta_mysql_cloud(self):
        config = {
            'user': 'user',
            'password': 'xxxxx',
            'host': 'server_name',
            'database': 'teste',
            'port': 3306,
            'raise_on_warnings': True,
        }
        conn3 = mysql.connector.connect(**config)
        return conn3
    
    """def conecta_oracle(self):
        # Connect as user "hr" with password "welcome" to the "oraclepdb" service running on this computer.
        host = 'hr'
        user = 'welcome'
        db_s = 'localhost/orclpdb'
        
        conn3 = cx_Oracle.connect(host, user, db_s)

        return conn3"""