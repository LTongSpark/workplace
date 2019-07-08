#-*-encoding:utf-8-*-
import numpy as np
import pandas as pd
stus_score = pd.DataFrame([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]] ,columns=("chinese",'eh'))
print(stus_score)
print(stus_score.shape)
q = np.array([[0.4], [0.6]])
result = np.dot(stus_score, q)

# print(np.array(result).reshape((stus_score.shape[0],1)))

stus_score["group"] = np.where(stus_score["eh"] > 82 ,"high" ,"low")
stus_score["avg"] = result
stus_score["result"] = 1
stus_score.set_index("group" ,inplace=False)
# stus_score.sort_index(by=["eh"] ,inplace=True)
print(stus_score)
print(stus_score.ix[3])