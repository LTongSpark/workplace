#-*-encoding:utf-8-*-

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
import pymysql
import numpy as np


mysql_cn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='security_info')
data_black = pd.read_sql('select * from ti_ua_black_call_info_d;', con=mysql_cn)
data_black.replace(to_replace="NULL", value=np.nan, inplace=True)
data_black["imei"] = data_black["imei"].str.replace("[a-zA-Z]","10")
data_black["opp_imei"] = data_black["opp_imei"].str.replace("[a-zA-Z]","10")
data_black.replace(to_replace="", value=np.nan, inplace=True)
data_black["ci"] = data_black["ci"].str.replace("|" ,"")
data_black["opp_ci"] = data_black["opp_ci"].str.replace("|","")

# 首次通话时间
first_call_date = pd.to_datetime(data_black["first_call_date"])
first_call_date_time = pd.DatetimeIndex(first_call_date)
data_black["first_call_date_year"] = first_call_date_time.year
data_black["first_call_date_month"] = first_call_date_time.month
data_black["first_call_date_day"] = first_call_date_time.day
data_black["first_call_date_week"] = first_call_date_time.week
data_black["first_call_date_hour"] = first_call_date_time.hour
data_black["first_call_date_minute"]  = first_call_date_time.minute
data_black["first_call_date_seconds"] = first_call_date_time.second

# 把入网时间拆分成不同的时间
time = pd.to_datetime(data_black['innet_date'])
time_value = pd.DatetimeIndex(time)
data_black["inner_year"] = time_value.year
data_black["inner_month"] = time_value.month
data_black["inner_day"] = time_value.day
data_black["inner_week"] = time_value.week
data_black["inner_hour"] = time_value.hour
data_black["inner_minute"] = time_value.minute
data_black["inner_seconds"] = time_value.second

# 开始时间
start_time = pd.to_datetime(data_black["start_time"])
start_time_value = pd.DatetimeIndex(start_time)
data_black["start_time_year"] = start_time_value.year
data_black["start_time_month"] = start_time_value.month
data_black["start_time_day"] = start_time_value.day
data_black["start_time_week"] = start_time_value.week
data_black["start_time_hour"] = start_time_value.hour
data_black["start_time_minute"] = start_time_value.minute
data_black["start_time_seconds"] = start_time_value.second

# 结束时间
end_time = pd.to_datetime(data_black["end_time"])
end_time_value = pd.DatetimeIndex(end_time)
data_black["end_time_year"] = end_time_value.year
data_black["end_time_month"] = end_time_value.month
data_black["end_time_day"] = end_time_value.day
data_black["end_time_week"] = end_time_value.week
data_black["end_time_hour"] = end_time_value.hour
data_black["end_time_minute"] = end_time_value.minute
data_black["end_time_seconds"] = end_time_value.second

# 位置码
data_black["lac"] = data_black["lac"].str.replace("[A,a]","10")
data_black["lac"] = data_black["lac"].str.replace("[B,b]","11")
data_black["lac"] = data_black["lac"].str.replace("[C,c]","12")
data_black["lac"] = data_black["lac"].str.replace("[D,d]","13")
data_black["lac"] = data_black["lac"].str.replace("[E,e]","14")
data_black["lac"] = data_black["lac"].str.replace("[F,f]","15")
# 小区码
data_black["ci"] = data_black["ci"].str.replace("[A,a]", "10")
data_black["ci"] = data_black["ci"].str.replace("[B,b]", "11")
data_black["ci"] = data_black["ci"].str.replace("[C,c]", "12")
data_black["ci"] = data_black["ci"].str.replace("[D,d]", "13")
data_black["ci"] = data_black["ci"].str.replace("[E,e]", "14")
data_black["ci"] = data_black["ci"].str.replace("[F,f]", "15")

# 对端位置码
data_black["opp_lac"] = data_black["opp_lac"].str.replace("[A,a]", "10")
data_black["opp_lac"] = data_black["opp_lac"].str.replace("[B,b]", "11")
data_black["opp_lac"] = data_black["opp_lac"].str.replace("[C,c]", "12")
data_black["opp_lac"] = data_black["opp_lac"].str.replace("[D,d]", "13")
data_black["opp_lac"] = data_black["opp_lac"].str.replace("[E,e]", "14")
data_black["opp_lac"] = data_black["opp_lac"].str.replace("[F,f]", "15")
# 对端小区码
data_black["opp_ci"] = data_black["opp_ci"].str.replace("[A,a]", "10")
data_black["opp_ci"] = data_black["opp_ci"].str.replace("[B,b]", "11")
data_black["opp_ci"] = data_black["opp_ci"].str.replace("[C,c]", "12")
data_black["opp_ci"] = data_black["opp_ci"].str.replace("[D,d]", "13")
data_black["opp_ci"] = data_black["opp_ci"].str.replace("[E,e]", "14")
data_black["opp_ci"] = data_black["opp_ci"].str.replace("[F,f]", "15")

data_black.fillna(value=0,inplace=True)

print(data_black.head(10))

data_white = pd.read_sql('select * from ti_ua_white_call_info_d;', con=mysql_cn)
data_white.replace(to_replace="NULL", value=np.nan, inplace=True)
data_white.replace(to_replace="", value=np.nan, inplace=True)
data_white["ci"] = data_white["ci"].str.replace("|", "")
data_white["opp_ci"] = data_white["opp_ci"].str.replace("|","")
# 首次通话时间
first_call_date = pd.to_datetime(data_white["first_call_date"])
first_call_date_time = pd.DatetimeIndex(first_call_date)
data_white["first_call_date_year"] = first_call_date_time.year
data_white["first_call_date_month"] = first_call_date_time.month
data_white["first_call_date_day"] = first_call_date_time.day
data_white["first_call_date_week"] = first_call_date_time.week
data_white["first_call_date_hour"] = first_call_date_time.hour
data_white["first_call_date_minute"] = first_call_date_time.minute
data_white["first_call_date_seconds"] = first_call_date_time.second

# 把入网时间拆分成不同的时间
time = pd.to_datetime(data_white['innet_date'])
time_value = pd.DatetimeIndex(time)
data_white["inner_year"] = time_value.year
data_white["inner_month"] = time_value.month
data_white["inner_day"] = time_value.day
data_white["inner_week"] = time_value.week
data_white["inner_hour"] = time_value.hour
data_white["inner_minute"] = time_value.minute
data_white["inner_seconds"] = time_value.second

# 开始时间
start_time = pd.to_datetime(data_white["start_time"])
start_time_value = pd.DatetimeIndex(start_time)
data_white["start_time_year"] = start_time_value.year
data_white["start_time_month"] = start_time_value.month
data_white["start_time_day"] = start_time_value.day
data_white["start_time_week"] = start_time_value.week
data_white["start_time_hour"] = start_time_value.hour
data_white["start_time_minute"] = start_time_value.minute
data_white["start_time_seconds"] = start_time_value.second

# 结束时间
end_time = pd.to_datetime(data_white["end_time"])
end_time_value = pd.DatetimeIndex(end_time)
data_white["end_time_year"] = end_time_value.year
data_white["end_time_month"] = end_time_value.month
data_white["end_time_day"] = end_time_value.day
data_white["end_time_week"] = end_time_value.week
data_white["end_time_hour"] = end_time_value.hour
data_white["end_time_minute"] = end_time_value.minute
data_white["end_time_seconds"] = end_time_value.second

# 位置码
data_white["lac"] = data_white["lac"].str.replace("[A,a]", "10")
data_white["lac"] = data_white["lac"].str.replace("[B,b]", "11")
data_white["lac"] = data_white["lac"].str.replace("[C,c]", "12")
data_white["lac"] = data_white["lac"].str.replace("[D,d]", "13")
data_white["lac"] = data_white["lac"].str.replace("[E,e]", "14")
data_white["lac"] = data_white["lac"].str.replace("[F,f]", "15")
# 小区码
data_white["ci"] = data_white["ci"].str.replace("[A,a]", "10")
data_white["ci"] = data_white["ci"].str.replace("[B,b]", "11")
data_white["ci"] = data_white["ci"].str.replace("[C,c]", "12")
data_white["ci"] = data_white["ci"].str.replace("[D,d]", "13")
data_white["ci"] = data_white["ci"].str.replace("[E,e]", "14")
data_white["ci"] = data_white["ci"].str.replace("[F,f]", "15")

# 对端位置码
data_white["opp_lac"] = data_white["opp_lac"].str.replace("[A,a]", "10")
data_white["opp_lac"] = data_white["opp_lac"].str.replace("[B,b]", "11")
data_white["opp_lac"] = data_white["opp_lac"].str.replace("[C,c]", "12")
data_white["opp_lac"] = data_white["opp_lac"].str.replace("[D,d]", "13")
data_white["opp_lac"] = data_white["opp_lac"].str.replace("[E,e]", "14")
data_white["opp_lac"] = data_white["opp_lac"].str.replace("[F,f]", "15")
# 对端小区码
data_white["opp_ci"] = data_white["opp_ci"].str.replace("[A,a]", "10")
data_white["opp_ci"] = data_white["opp_ci"].str.replace("[B,b]", "11")
data_white["opp_ci"] = data_white["opp_ci"].str.replace("[C,c]", "12")
data_white["opp_ci"] = data_white["opp_ci"].str.replace("[D,d]", "13")
data_white["opp_ci"] = data_white["opp_ci"].str.replace("[E,e]", "14")
data_white["opp_ci"] = data_white["opp_ci"].str.replace("[F,f]", "15")
data_white.fillna(value=0, inplace=True)
print(data_white.head(10))

data_join = pd.concat([data_white, data_black])

# 分割数据集到训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(data_join[[
                                                                'serv_no',  #主叫号码
                                                                'opp_serv_no', #被叫号码
                                                                'cert_typ_id',#是否实名登记
                                                                'c_hplmn1',#归属省份
                                                                'c_hplmn3',#归属县市
                                                                'user_id',#用户标识
                                                                'prod_id',#产品标识
                                                                'brand_code',#品牌
                                                                'acct_id',#账户标识
                                                                'user_type',#用户类别
                                                                #'tele_type', #电信类型
                                                                #'pay_type',#付费类型
                                                                'chrg_type',#计费类型
                                                                'cust_id',#客户标识
                                                                #'calling_type',#呼叫类型
                                                                'call_type',#通话类型
                                                                'net_call_type',#网内外类型
                                                                'toll_type',  #长途类型
                                                                'roam_type',#漫游类型
                                                                'net_type',#网络类型
                                                                'imei',#imei
                                                                'opp_imei',#对端imei
                                                                #'bs_type',# 基站类型
                                                                'third_no', #第三方号码
                                                                #'serv_fee_type',#计费业务类型
                                                                #'serv_fee_code',#计费义务代码标识
                                                                'media_call_flag',#视频呼叫标志
                                                                #'edge_roam_flag',#边界漫游标志
                                                                #'specl_no',# 特殊号码
                                                                #'specl_no_type', #特殊号码类型
                                                                'accs_no',#接入号码
                                                                #'accs_no_type',#接入号码类型
                                                                #'roam_cntry_code',#本端漫游国家码
                                                                #'opp_roam_cntry_code',#对端漫游国际码
                                                                #'home_net_type', #本端网络类型
                                                                #'opp_home_net_type',#对端网络类型
                                                                #'operator_code',#本端运营商
                                                                'opp_operator_code',#对端运营商
                                                                #'home_cntry_code',#本端归属国家码
                                                                #'opp_home_cntry_code',#对端归属国家码
                                                                'home_city_code',  #本端归属地区号
                                                                'opp_home_city_code', #对端归属地区号
                                                                'call_dur', #通话时长
                                                                'first_call_date_year',#首次通话的年份
                                                                'first_call_date_month',#首次通话的月份
                                                                'first_call_date_day',#首次通话的天数
                                                                'first_call_date_week',#首次通话的周数
                                                                'first_call_date_hour',#首次通话的小时 在这一天内
                                                                'first_call_date_minute',
                                                                'first_call_date_seconds',
                                                                'inner_year',
                                                                'inner_month',
                                                                'inner_day',
                                                                'inner_week',
                                                                'inner_hour',
                                                                'inner_minute',
                                                                'inner_seconds',
                                                                'start_time_year',
                                                                'start_time_month',
                                                                'start_time_day',
                                                                'start_time_week',
                                                                'start_time_hour',
                                                                'start_time_minute',
                                                                'start_time_seconds',
                                                                'end_time_year',
                                                                'end_time_month',
                                                                'end_time_day',
                                                                'end_time_week',
                                                                'end_time_hour',
                                                                'end_time_minute',
                                                                'end_time_seconds',
                                                                'lac', #位置码
                                                                'ci',#小区码
                                                                'opp_lac',#对端位置码
                                                                'opp_ci'#对端小区码

                        ]], data_join['hb_flag'], test_size=0.25)

# 进行标准化处理
std = StandardScaler()
x_train = std.fit_transform(x_train)
x_test1 = std.fit_transform(x_test)
lg = LogisticRegression(C=1.0)

lg.fit(x_train, y_train)


y_predict = lg.predict(x_test1)
print("准确率：", lg.score(x_test1, y_test))
print("召回率：", classification_report(y_test, y_predict, labels=[1, 2], target_names=["black", "white"]))






