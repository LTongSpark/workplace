# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import xlrd
import xlwt
data = pd.read_csv('C:/Users/Administrator/Desktop/tong.csv',encoding='gbk')
data_df = data[['计费号码','通话类型','开始时间','时长']]

data_df = data_df[~data_df['计费号码'].isin(['计费号码'])]
data_df['开始时间'] = pd.to_datetime(data_df['开始时间']).apply(lambda x:x.day)

data_df['通话类型'] = data_df['通话类型'].str[1:2]



data_df.groupby(['计费号码','通话类型','开始时间']).count().reset_index()
data_df.columns=[]


