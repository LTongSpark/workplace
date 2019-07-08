# -*-encoding:utf-8-*-
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.externals import joblib
import pymysql
import warnings
import numpy as np

mysql_cn = pymysql.connect(host='10.212.4.34', port=3306, user='root', passwd='root', db='security_info')
data_black = pd.read_sql('select * from ti_ua_black_user_info_d_20190108;', con=mysql_cn)
data_black["c_cust_cert_code"] = data_black["c_cust_cert_code"].str.replace('[a-zA-Z]' ,'10')
data_black.replace(to_replace="", value=np.nan, inplace=True)
data_black.replace(to_replace="NULL", value=np.nan, inplace=True)
data_black.fillna(value=0, inplace=True)
warnings.filterwarnings("ignore")

# 设置省份
data_black["province"] = data_black["c_cust_cert_code"].str[0:2]
#设置地级市
data_black["prefecture"] = data_black["c_cust_cert_code"].str[2:4]
#设置州县
data_black["country"] = data_black["c_cust_cert_code"].str[4:6]

# 把入网时间拆分成不同的时间
time = pd.to_datetime(data_black['innet_date'])
time_value = pd.DatetimeIndex(time)
data_black["day"] = time_value.day
data_black["week"] = time_value.week
data_black["hour"] = time_value.hour
data_black["second"] = time_value.second
data_black["month"] = time_value.month

# 把关联号码的时间拆分成不同的时间
else_time = pd.to_datetime(data_black['else_innet_date'])
else_time_value = pd.DatetimeIndex(else_time)
data_black["else_day"] = else_time_value.day
data_black["else_week"] = else_time_value.week
data_black["else_hour"] = else_time_value.hour
data_black["else_second"] = else_time_value.second
data_black["else_month"] = else_time_value.month
# 设置黑名单
data_black["hb_flag"] = 1

data_white = pd.read_sql('select * from ti_ua_white_user_info_d_20190108;', con=mysql_cn)
data_white = pd.read_sql('select * from ti_ua_white_user_info_d_20190108 WHERE LENGTH(c_cust_cert_code) =18;', con=mysql_cn)

data_white["c_cust_cert_code"] = data_white["c_cust_cert_code"].str.replace('[a-zA-Z]', '10')
data_white.replace(to_replace="NULL", value=np.nan, inplace=True)
data_white.replace(to_replace="", value=np.nan, inplace=True)
data_white.fillna(value=0, inplace=True)
# 设置省份
data_white["province"] = data_white["c_cust_cert_code"].str[0:2]

# 把入网时间拆分成不同的时间
time = pd.to_datetime(data_white['innet_date'])
time_value = pd.DatetimeIndex(time)
data_white["day"] = time_value.day
data_white["week"] = time_value.week
data_white["hour"] = time_value.hour
data_white["second"] = time_value.second
data_white["month"] = time_value.month

# 把关联号码的时间拆分成不同的时间
else_time = pd.to_datetime(data_white['else_innet_date'])
else_time_value = pd.DatetimeIndex(else_time)
data_white["else_day"] = else_time_value.day
data_white["else_week"] = else_time_value.week
data_white["else_hour"] = else_time_value.hour
data_white["else_second"] = else_time_value.second
data_white["else_month"] = else_time_value.month

# 设置白名单
data_white["hb_flag"] = 2

data_join = pd.concat([data_white, data_black] ,ignore_index=True)
# print(type(data_join))
# 分割数据集到训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(data_join[['phone_no', 'cust_id', 'user_id', 'c_cust_cert_code',
                                                               'age', 'c_real_name_flag', 'create_org_id', 'sts',
                                                               'call_flag', 'else_phone_no','else_cust_id', 'else_create_org_id',
                                                               'else_sts', 'else_1_money', 'else_2_money',
                                                               'else_3_money',"province","day" ,"week" ,"hour",
                                                               "second" ,"month" ,"else_day" ,"else_week" ,"else_second" ,
                                                               "else_month",'prefecture' ,'country'
                                                               ]], data_join['hb_flag'], test_size=0.25)

phoneNum= open(r'/home/oycm/shuju/phoneNum.txt', 'w')
if_black = open(r'/home/oycm/shuju/if_black.txt', 'w')
base_dir = "/home/oycm/shuju"

with open(base_dir + '/static_phoneNum.txt', 'w+') as f:
    for i in x_test["phone_no"].values:
        f.write(str(i) + "\r")

# 进行标准化处理
std = StandardScaler()
x_train = std.fit_transform(x_train)
x_test1 = std.fit_transform(x_test)
lg = LogisticRegression(C=1.5 ,n_jobs=2)

lg.fit(x_train, y_train)

# 保存训练好的模型
joblib.dump(lg, "/home/oycm/modle/static_mode.pkl")

# #加载模型
# model = joblib.load("/home/oycm/modle/static_mode.pkl")
# y_predict = model.predict(x_test1)

y_predict = lg.predict(x_test1)

with open(base_dir + '/static_if_black.txt', 'w+') as f:
    for i in y_predict:
        f.write(str(i) + "\r")
# print("准确率：", lg.score(x_test1, y_test))
with open(base_dir + '/static_phoneNum.txt', 'r') as f:
    json_list = f.read().replace('\r', '').replace('\n', ',').split(',')

with open(base_dir + '/static_if_black.txt', 'r') as f:
    scores_list = f.read().replace('\r', '').replace('\n', ',').split(',')

with open(base_dir + '/static_result.txt', 'w+') as f:
    for index in zip(scores_list, json_list):
        f.write(index[0] + "," + index[1] + "\r")

print("准确率：", lg.score(x_test1, y_test))
print("召回率：", classification_report(y_test, y_predict, labels=[1, 2], target_names=["black", "white"]))
