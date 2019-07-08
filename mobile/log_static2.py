# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.externals import joblib
from sqlalchemy import create_engine
import warnings
import numpy as np


class static(object):
    '''
    初始化
    '''
    def __init__(self):
        self.host = "10.212.4.34"
        self.port = 3306
        self.user = "root"
        self.pass_word = "Admin@123"
        self.db = "security_info"
        self.engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.
                                    format(self.user, self.pass_word, self.host, self.port, self.db), echo=False)
        self.pkl = "/home/oycm/modle/static_mode.pkl"

    def parse_data(self, datafame, flag):
        '''
        解析数据
        :param datafame: 数据
        :param flag: 白名单[2]和黑名单[1]
        :return: dataframe
        '''

        datafame["c_cust_cert_code"] = datafame["c_cust_cert_code"].str.replace('[a-zA-Z]', '10')
        datafame.replace(to_replace="", value=np.nan, inplace=True)
        datafame.replace(to_replace="NULL", value=np.nan, inplace=True)
        datafame.fillna(value=0, inplace=True)
        # 设置省份
        datafame["province"] = datafame["c_cust_cert_code"].str[0:2]
        # 设置地级市
        datafame["prefecture"] = datafame["c_cust_cert_code"].str[2:4]
        # 设置州县
        datafame["country"] = datafame["c_cust_cert_code"].str[4:6]

        datafame["else_phone_no"] = datafame.groupby("else_phone_no")
        # 把入网时间拆分成不同的时间
        self.parse_time(datafame, datafame["innet_date"])
        # 把关联号码的时间拆分成不同的时间
        self.parse_else_time(datafame, datafame['else_innet_date'])
        # 设置黑名单
        datafame["hb_flag"] = flag

    def parse_data_black(self):
        '''
        解析黑名单数据
        :return:
        '''
        data_black = pd.read_sql('select * from ti_ua_black_user_info_d_20190108;', con=self.engine)
        self.parse_data(data_black, 1)
        return data_black

    def parse_data_white(self):
        '''
        解析白名单数据
        :return:
        '''
        #data_white = pd.read_sql('select * from ti_ua_white_user_info_d_20190108;', con=self.engine)
        data_white = pd.read_sql('select * from ti_ua_white_user_info_d_20190108 WHERE LENGTH(c_cust_cert_code) =18 limit 10 ;',
                                 con=self.engine)
        self.parse_data(data_white, 2)
        return data_white

    def run(self):
        '''
        主函数
        :return:
        '''
        warnings.filterwarnings("ignore")
        black = self.parse_data_black()
        white = self.parse_data_white()
        data = pd.concat([black, white] ,ignore_index=True)

        # 分割数据集到训练集和测试集
        # x_train, x_test, y_train, y_test = train_test_split(
        #     data[['phone_no', 'age', 'c_real_name_flag', 'create_org_id', 'sts',
        #           'call_flag', 'else_phone_no', 'else_cust_id', 'else_create_org_id',
        #           'else_sts', 'else_1_money', 'else_2_money',
        #           'else_3_money', "province", "day", "week", "hour",
        #           "second", "month", "else_day", "else_week", "else_second",
        #           "else_month", 'prefecture', 'country'
        #           ]], data['hb_flag'], test_size=0.25)

        x_train, x_test, y_train, y_test = train_test_split(
            data[['phone_no', 'age', 'c_real_name_flag',  'sts','call_flag', 'else_phone_no',
                  'else_sts', 'else_1_money', 'else_2_money',
                  'else_3_money', "province", "day", "week", "hour",
                  "second", "month", "else_day", "else_week", "else_second",
                  "else_month", 'prefecture', 'country'
                  ]], data['hb_flag'], test_size=0.25)

        # 进行标准化处理
        std = StandardScaler()
        x_train = std.fit_transform(x_train.loc[:,x_train.columns != "phone_no"])
        print(x_train.shape())
        x_test1 = std.fit_transform(x_test)
        # #用逻辑回归
        # lg = LogisticRegression(C=1.5, n_jobs=2)
        # lg.fit(x_train, y_train)
        # y_predict = lg.predict(x_test1)
        # print("准确率", lg.score(x_test, y_test))
        #result = pd.DataFrame({"phonenm": x_test['phone_no'], 'result': y_predict})

        #用随机森林
        param = {"n_estimators": [120, 200, 300, 500, 800, 1200], "max_depth": [5, 8, 15, 25, 30]}
        #用网格搜索与交叉验证
        rf = RandomForestClassifier()
        gc = GridSearchCV(rf, param_grid=param, cv=5)

        gc.fit(x_train, y_train)
        print("准确率" ,gc.score(x_test.loc[:,x_test.columns != "phone_no"] ,y_test))
        print("最好的参数" ,gc.best_params_)


        # 保存训练好的模型
        #joblib.dump(lg, self.pkl)

        # #加载模型
        # model = joblib.load("/home/oycm/modle/static_mode.pkl")
        # y_predict = model.predict(x_test1)

        #保存数据
        #self.save_result(result)
        # print("准确率：", lg.score(x_test1, y_test))
        # print("召回率：", classification_report(y_test, y_predict, labels=[1, 2], target_names=["black", "white"]))

    def save_result(self,dataframe):
        '''
        保存数据
        :param dataframe:
        :return:
        '''
        dataframe.to_sql("result_static" ,con=self.engine ,index=False,if_exists="replace")

    def parse_time(self, data, time):
        '''
        解析时间
        :param data:
        :param time:
        :return:
        '''
        time = pd.to_datetime(time)
        time_value = pd.DatetimeIndex(time)
        data["day"] = time_value.day
        data["week"] = time_value.week
        data["hour"] = time_value.hour
        data["second"] = time_value.second
        data["month"] = time_value.month

    def parse_else_time(self, data, time):
        time = pd.to_datetime(time)
        time_value = pd.DatetimeIndex(time)
        data["else_day"] = time_value.day
        data["else_week"] = time_value.week
        data["else_hour"] = time_value.hour
        data["else_second"] = time_value.second
        data["else_month"] = time_value.month


if __name__ == '__main__':
    static().run()

