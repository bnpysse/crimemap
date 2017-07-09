# encoding=utf-8
# Created by {donglida} on {17-7-9} {下午3:57}

import pymysql
import dbconfig
connection = pymysql.connect(host='192.168.1.20',
                             user=dbconfig.db_user,
                             passwd=dbconfig.db_password)
try:
    with connection.cursor() as cursor:
        sql = "CREATE DATABASE IF NOT EXISTS crimemap"
        cursor.execute(sql)
        sql = """
        CREATE TABLE IF NOT EXISTS crimemap.crimes(
        id int NOT NULL AUTO_INCREMENT,
        latitude FLOAT(10,6),
        longitude FLOAT (10, 6),
        date DATETIME,
        category VARCHAR (50),
        description VARCHAR (1000),
        update_at TIMESTAMP ,
        PRIMARY KEY(id)
        )
        """
        cursor.execute(sql)
        connection.commit()
finally:
    connection.close()
;