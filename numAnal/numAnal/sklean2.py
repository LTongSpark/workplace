#-*-encoding:utf-8-*-
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler,StandardScaler,Imputer
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA
import jieba
import numpy as np

sent = jieba.cut("中国移动通信集团贵州/省公司/网络与信息安全管理中心")
sent3 = jieba.cut("已补充，请罗笑然对今日身份证黑名单纳入系统,谢谢。")
sent1 = list(sent)
sent2 = list(sent3)
# print(sent1)
# print(type(sent1))
sent_word = ' '.join(sent1)
sent_word1= ' '.join(sent2)
# print(sent_word)
# print(type(sent_word))

'''
tf :词频
idf：逆文档频率指数
'''
stop_word = ["中国移动通信集团" ,'信息安全']
count = TfidfVectorizer(stop_words=stop_word)
# print([sent_word,sent_word1])
count_word = count.fit_transform([sent_word ,sent_word1])
# print(count.get_feature_names())
# print(count_word.toarray())


# 标椎化
std = StandardScaler()
std_str = std.fit_transform([[1,2,3],[2,3,4],[4,5,6]])
# print(std_str)

# 缺失值
im = Imputer(missing_values="NaN" ,strategy="mean",axis=0)
stat = im.fit_transform([[1, 2, 3], [2, np.nan, 4], [4, 5, 6]])
# print(stat)

# 降维 删除低方差的特征
var = VarianceThreshold(threshold=0.0)
data = var.fit_transform([[1, 2, 3], [1, 4, 4], [1, 5, 6]])
# print(data)

# 主成分分析降维
pca = PCA(n_components=0.9)
data = pca.fit_transform([[1, 2, 3], [1, 4, 4], [1, 5, 6]])
print(data)