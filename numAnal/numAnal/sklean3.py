#-*-encoding:utf-8-*-
import  pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
# 获取数据
taitan = pd.read_csv("")
# 处理数据
x = taitan[["pclass" ,'age' ,'sex']]
y = taitan["survived"]

# 缺失值处理
x["age"].fillna(x["age"].mean,inplace=True)

# 分割数据集到训练集合中
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

# 进行处理特征工程 one_hot编码
dict = DictVectorizer(sparse=False)

x_train = dict.fit_transform(x_train.to_dict(orient = "records"))
x_test = dict.fit_transform(x_test.to_dict(orient="records"))

# 用决策树进行预测
tree= DecisionTreeClassifier()

tree.fit(x_train ,y_train)

# 准确率
tree.score(x_test ,y_test)

