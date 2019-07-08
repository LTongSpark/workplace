#-*-encoding:utf-8-*-
from sklearn.feature_extraction import DictVectorizer

# 惊醒处理特征工程 特征——类别——one_hot编码
dict = DictVectorizer(sparse = False)
data= dict.fit_transform([{'city':'北京','tem':12}, {'city': '上海', 'tem': 13}, {'city': '深圳', 'tem': 14}])
print(dict.feature_names_)
print(data)

