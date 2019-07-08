#-*-encoding:utf-8-*-
import pandas as pd
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler
import numpy as np
import warnings
from sqlalchemy import create_engine

'''
链接数据库
'''
# 连接数据库的数据
Host = '10.212.4.34'
Port = '3306'
DataBase = 'security_info'
UserName = 'root'
PassWord = 'Admin@123'
# DB_URI的格式：dialect（mysql/sqlite）+driver://username:password@host:port/database?charset=utf8
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(UserName, PassWord, Host, Port, DataBase)
# 1、创建一个engine引擎
engine = create_engine(DB_URI, echo=False)

data = pd.read_sql('select * from ti_ua_user_innet_info_d;', con=engine)
data["c_cust_cert_code"] = data["c_cust_cert_code"].str.replace('[a-zA-z]', '10')
data.replace(to_replace="", value=np.nan, inplace=True)
data.replace(to_replace="NULL", value=np.nan, inplace=True)
data.fillna(value=0, inplace=True)
warnings.filterwarnings("ignore")
# 设置省份
data["province"] = data["c_cust_cert_code"].str[0:2]
data['prefecture']  =data['c_cust_cert_code'].str[2,4]
data['country']  =data['c_cust_cert_code'].str[4,6]

# 把入网时间拆分成不同的时间
time = pd.to_datetime(data['innet_date'])
time_value = pd.DatetimeIndex(time)
data["day"] = time_value.day
data["week"] = time_value.week
data["hour"] = time_value.hour
data["second"] = time_value.second
data["month"] = time_value.month

# 把关联号码的时间拆分成不同的时间
else_time = pd.to_datetime(data['else_innet_date'])
else_time_value = pd.DatetimeIndex(else_time)
data["else_day"] = else_time_value.day
data["else_week"] = else_time_value.week
data["else_hour"] = else_time_value.hour
data["else_second"] = else_time_value.second
data["else_month"] = else_time_value.month

x_test = data[['phone_no', 'cust_id', 'user_id', 'c_cust_cert_code',
               'age', 'c_real_name_flag', 'create_org_id', 'sts',
               'call_flag', 'else_phone_no', 'else_cust_id', 'else_create_org_id',
               'else_sts', 'else_1_money', 'else_2_money',
               'else_3_money', "province", "day", "week", "hour",
               "second", "month", "else_day", "else_week", "else_second", "else_month",
               "prefecture",'country']]

print(x_test)

std = StandardScaler()
x_test1 = std.fit_transform(x_test)
#加载模型
model = joblib.load("/home/oycm/modle/static_mode.pkl")
y_predict = model.predict(x_test1)
result = pd.DataFrame({"phonenum":x_test["phone_no"] ,"result":y_predict})
result.to_sql("table" ,index=False ,if_exists="append" ,con=engine)

