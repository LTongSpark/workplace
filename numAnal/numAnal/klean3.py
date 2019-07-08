#-*-encoding:utf-8-*-
from sklearn.datasets import load_iris,fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

li = load_iris()
# print(li.data)
# print(li.target)

'''
训练集
x_train
y_train
测试集
x_text
y_text
'''
x_train, x_text, y_train, y_text= train_test_split(li.data ,li.target , test_size = 0.25)

# print("训练集数据" ,x_train,y_train)
# print("测试集数据" , x_text,y_text)

# 拿出数据
news = fetch_20newsgroups(subset="all")
# 切分
x_train, x_text, y_train, y_text = train_test_split(news.data, news.target, test_size=0.25)

# 对数据进行过特征性的提取
tf = TfidfVectorizer()
x_train = tf.fit_transform(x_train)
print(tf.get_feature_names())
x_text = tf.transform(x_text)

# 进行朴素贝叶斯算法的 预测

nb = MultinomialNB(alpha=1.0)

nb.fit(x_train,y_train)
# 预测
_pred = nb.predict(y_text)

# 准确度
nb.score(x_text ,y_text)

# 精确率和召回率

classification_report(y_text ,_pred , target_names=news.target_names)




