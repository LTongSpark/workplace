# -*-encoding:utf-8-*-
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.externals import joblib
import mobile.read_file
import pymysql

l = []
mysql_cn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='mobile')

data_black = pd.read_csv("C:/Users/28670/Desktop/black.txt", header=None, sep='!')
data_black.fillna(value=0, inplace=True)
data_black[56] = 1

data_white = pd.read_csv("C:/Users/28670/Desktop/white.txt", header=None, sep='!')
data_white.fillna(value=0, inplace=True)
data_white[56] = 0
data_join = pd.concat([data_white, data_black])
#print("data_join", data_join)
# 分割数据集到训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(data_join[
                                                        [1, 2, 3, 4, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                                                         21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
                                                         37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
                                                         53, 54, 55]], data_join[56], test_size=0.25)
# 进行标准化处理
base_dir = "D:/mr"

#print('X-text', x_test)

with open(base_dir + '/scores.txt', 'w+') as f:
    for i in x_test[1].values:
        f.write(str(i) + "\r")
std = StandardScaler()
# x_train = std.fit_transform(x_train)
x_test1 = std.fit_transform(x_test)
lg = LogisticRegression(C=1.0 , solver='liblinear')
#
# lg.fit(x_train, y_train)
# joblib.dump(lg,"./temp.pkl")
#
# y_predict = lg.predict(x_test1)
modle = joblib.load("./temp.pkl")
y_predict = modle.predict(x_test1)

with open(base_dir + '/json.txt', 'w+') as f:
    for i in y_predict:
        f.write(str(i) + "\r")
# print("准确率：", lg.score(x_test1, y_test))
with open(base_dir + '/json.txt', 'r') as f:
    json_list = f.read().replace('\r', '').replace('\n', ',').split(',')

with open(base_dir + '/scores.txt', 'r') as f:
    scores_list = f.read().replace('\r', '').replace('\n', ',').split(',')

with open(base_dir + '/words.txt', 'w+') as f:
    for index in zip(scores_list, json_list):
        f.write(index[0] + "\t\t" + index[1] + "\r")


print("召回率：", classification_report(y_test, y_predict, labels=[1, 0], target_names=["black", "white"]))
