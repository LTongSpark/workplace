#-*-encoding:utf-8-*-
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split ,GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

data = pd.read_csv("")

# 处理数据
# 缩小数据，查询数据删选
data = data.query("x > 1.0 & x < 1.25 & y >1.5 & y < 1.75")

# 处理时间
time_value = pd.to_datetime(data["time"] ,unit="s")
time = pd.DatetimeIndex(time_value)

data["hour"] = time.hour
# 在pd中axis = 0代表行 ，axis=1 代表列
# 在sklean中axis = 1代表行，axis=0代表列
data = pd.drop("time" ,axis =1)

#把签到的数量少于那个的目标位置删除
place_count = data.groupby("place_id").count()
tf = place_count[place_count.row_id > 3].reset_index()
data = data[data["place_id"].isin(tf.place_id)]
# 取出特征值和目标值
y = data["place_id"]
x = pd.drop("place_id" ,axis = 1)

# 进行数据的分割
x_train,x_test ,y_train ,y_test = train_test_split(x,y ,test_size=0.25)
# 标椎化
std = StandardScaler()
x_train = std.fit_transform(x_train)
x_test = std.transform(x_test)

# 进行算法的流程
knn = KNeighborsClassifier(n_neighbors=5)
# knn.fit(x_train,y_train)
# # 得到预测结果
# y_predict= knn.predict(x_test)
# # 得到准确率
# y_score = knn.score(x_test,y_test)
praram = {"n_neighbors":[1,2,3,4,5]}
# 进行网格搜索
gd = GridSearchCV(knn,param_grid=praram ,cv= 2)
gd.fit(x_train ,y_train)
gd.predict(x_test)
gd.score(x_test ,y_test)
# 在交叉验证中最好的结果
print(gd.best_score)
#在交叉验证中最号的模型
print(gd.best_estimator_)