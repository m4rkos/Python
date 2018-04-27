### Author: Marcos Eduardo - m4rkos

#### First: 
NOTE: This application use python version 3.

Do you have create a database (ex: teste) and execute the ./SQL/contatos.sql

## Mysql

Install `pip install mysql-connector-python-rf`

    import mysql.connector

    class Connection():
        def conecta_mysql(self):
            config = {
                'user': 'root',
                'password': '',
                'host': '127.0.0.1',
                'database': 'test',
                'raise_on_warnings': True,
            }
            conn2 = mysql.connector.connect(**config)
            return conn2
***

or

Install `pip install pymysql`

    import pymysql

    class Connection():
        def connect_mysql2():
            connection = pymysql.connect(user='x', passwd='x',
                                    host='x',
                                    database='x')

            cursor = connection.cursor()

## Sql Server

Install `pip install pypyodbc` for python 3.6 

or for python 2.7 `pip install pyodbc`

    import pypyodbc

    class Connection():
        def conecta_msql(self):
            conn = pypyodbc.connect(
                'DRIVER={SQL Server};'
                'SERVER=pc_user;'
                'DATABASE=teste;'
                'UID=sa;'
                'PWD=xxxxxx'
                )
            return conn

***

## Oracle

Install `python -m pip install cx_Oracle --upgrade`

    from __future__ import print_function
    import cx_Oracle

    class Connection():
        def conecta_oracle(self):
            # Connect as user "hr" with password 
            #"welcome" to the "oraclepdb" service running on this computer.
            connection = cx_Oracle.connect("hr", "welcome", "localhost/orclpdb")

            return connection

>Exemplo select:

    cursor = connection.cursor()
        cursor.execute(
            SELECT first_name, last_name
            FROM employees
            WHERE department_id = :did AND employee_id > :eid,
            did = 50,
            eid = 190)
        for fname, lname in cursor:
            print("Values:", fname, lname)
***

## Speech

Python 3

`pip install pyttsx3`

    import pyttsx3

    engine = pyttsx3.init()
    engine.say('Oi ' + var)
    engine.setProperty('rate',100)
    engine.runAndWait()