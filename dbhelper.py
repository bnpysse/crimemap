# encoding=utf-8
# Created by {donglida} on {17-7-12} {上午1:11}

import pymysql
import dbconfig

class DBHelper:

    def connect(self, database='crimemap'):
        return pymysql.connect(host='192.168.1.20',
                               port=3306,
                               user=dbconfig.db_user,
                               passwd=dbconfig.db_password,
                               db=database)

    def get_all_inputs(self):
        connection = self.connect()
        try:
            query = "SELECT description FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            connection.close()

    def add_input(self, data):
        connection = self.connect()
        try:
            query = "INSERT INTO crimes (description) VALUES(%s)".format(data)
            with connection.cursor() as cursor:
                cursor.execute(query, data)
                connection.commit()
        finally:
            connection.close()

    def clear_all(self):
        connection = self.connect()
        try:
            query = "DELETE FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute()
                connection.commit()
        finally:
            connection.close()

