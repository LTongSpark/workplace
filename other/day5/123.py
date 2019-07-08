#-*-encoding:utf-8-*-
import numpy as np
import pandas as pd
import pymysql
import numpy as np
from sqlalchemy import create_engine
import warnings


class static(object):
    def __init__(self):
        # 连接数据库的数据
        Host = '127.0.0.1'
        Port = '3306'
        DataBase = 'spark_home'
        UserName = 'root'
        PassWord = 'root'
        # DB_URI的格式：dialect（mysql/sqlite）+driver://username:password@host:port/database?charset=utf8
        self.DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(UserName, PassWord, Host, Port, DataBase)
        # 1、创建一个engine引擎
        self.engine = create_engine(self.DB_URI, echo=False)

    def parse(self,df1):
        df1.replace(to_replace="", value=np.nan, inplace=True)
        df1.replace(to_replace="NULL", value=np.nan, inplace=True)
        df1.replace(to_replace=".", value="", inplace=True)
        self.parse_time(df1,df1["timestamp"])
        return df1

    def run(self):
        warnings.filterwarnings("ignore")
        df1 = pd.read_sql('select * from qqq;' ,con=self.engine)
        self.parse(df1)
        print(df1.columns != "userId")
        df = df1.loc[:, df1.columns != "userId"]
        #把统计后的结果添加到原来的数据集中利用join
        df2 = df.groupby(["day"])['timestamp'].agg(["count"]).reset_index()
        df3 = df1.join(df2.set_index("day") ,on = 'day')

        print(df3)
        return df

    def run1(self):
        df1 = pd.read_sql('select * from qqq;', con=self.mysql_cn)
        self.parse(df1)
        return df1
    def save_mysql(self):
        data = self.run()
        dataframe = data[['userId' ,'day']]
        print(dataframe)
        dataframe.to_sql("123" ,con=self.engine ,if_exists="replace" ,index=False)

    def parse_time(self,data, time):
        time = pd.to_datetime(time)
        time_value = pd.DatetimeIndex(time)
        data["day"] = time_value.day
        data["week"] = time_value.week
        data["hour"] = time_value.hour
        data["second"] = time_value.second
        data["month"] = time_value.month

if __name__ == '__main__':
    df1 = static().run()
    print(df1)



