# -*-encoding:utf-8-*-
import pandas as pd
import numpy as np

df = pd.DataFrame({'key1':['a','a','b','b','a'],'key2':['one','two','one','two','one'],'data1':np.random.randn(5),'data2':np.random.randn(5)})
#处理数据
df.loc[df['key2'] =='one' ,'key2'] = 1
df.loc[df['key2'] =='two' ,'key2'] = 2

#onehot
x = pd.get_dummies(df,sparse=True)
x.drop(x.columns[x.std==0],axis=1,inplace=True)
print(x)
