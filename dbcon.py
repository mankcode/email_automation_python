from debugpy import connect
import pymysql


class DbCon:

    def __init__(self):
        self.host = 'host'
        self.user = 'user'
        self.password = 'pass'
        self.database = 'serwer'

    def __connect__(self):
        self.con = pymysql.connect(
            host=self.host, user=self.user, password=self.password, database=self.database)
        self.cursor = pymysql.connect(
            host=self.host, user=self.user, password=self.password, database=self.database).cursor()

    def single_data(self, sql):
        self.__connect__()
        self.cursor.execute(sql)
        for x in self.cursor:
            return x[0]
