#-*- coding: utf-8 -*-

import os
import time

import sqlite3

DEFAULT_DATABASE_FILE = "./database/sjxf.db"


class SjxfDatabase:

    def __init__(self, phone_number, database_path=DEFAULT_DATABASE_FILE):

        '''存放数据库的目录是否存在'''
        if not os.path.exists(os.path.dirname(database_path)):
            os.mkdir(os.path.dirname(database_path))

        self.__default_database = database_path
        self.__table_name = 'user' + str(phone_number)
#        print("默认数据库路径为{}".format(database_path))


    def __open_database(self):
        self.__sql_connection = sqlite3.connect(self.__default_database)
        self.__sql_cursor = self.__sql_connection.cursor()
#        print("打开数据库成功")


    '''判断表是否创建,如果没有创建则创建'''
    def __table_is_exist(self):
        self.__table_ji_fen_sql = "CREATE TABLE IF NOT EXISTS \"{}\"(" \
                                  " date TEXT PRIMARY KEY NOT NULL," \
                                  " total_points INTEGER NOT NULL," \
                                  " today_points INTEGER NOT NULL)".format(self.__table_name)
#        print(self.__table_ji_fen_sql)
        try:
            self.__sql_cursor.execute(self.__table_ji_fen_sql)
#            print("创建数据库成功")
            return True
        except sqlite3.Error as e:
#            print("创建数据库失败:{}".format(e.args[0]))
            return False

    def __close_database(self):
        self.__sql_cursor.close()
        self.__sql_connection.close()

    '''data = {'total_points':'', 'today_points':''}'''
    def insert_data(self, data:dict) ->bool: 

        if len(data.keys()) == 0:
            return False
        
        self.__open_database()
        self.__table_is_exist()

        self.__insert_sql = "INSERT INTO \"{}\" VALUES(\"{}\", \"{}\", \"{}\")".format(
                             str(self.__table_name),
                            #  str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),
                             str(time.strftime("%Y-%m-%d", time.localtime())),
                             int(data['total_points']),
                             int(data['today_points']))

#        print(self.__insert_sql)
        try:
            self.__sql_cursor.execute(self.__insert_sql)
            self.__sql_connection.commit()
            self.__close_database()
            return True
        except sqlite3.Error as e:
#            print("插入数据失败:{}".format(e.args[0]))
            self.__update_sql = "update \"{}\" set \"total_points\"=\"{}\", \"today_points\"={} "\
                                "where \"date\"=\"{}\"".format(
                                str(self.__table_name),
                                int(data['total_points']),
                                int(data['today_points']),
                                str(time.strftime("%Y-%m-%d", time.localtime())),
                                ) 

            self.__sql_cursor.execute(self.__update_sql)
            self.__close_database()
            return False


#data = {'total_points':'500', 'today_points': '15'}
#database = SjxfDatabase(13344445555)
#database.insert_data(data)
