import random
from sklearn.neighbors import NearestNeighbors
import numpy as np


class KnnData():
    def __init__(self,samples_df, N=2, k=2,dtypes=1):
        """
        :param samples_df:
        :param N: 倍数
        :param k: 临近个数
        :param dtypes: 要翻倍的标签类型
        """
        self.dtypes=dtypes
        self.n_samples,self.n_attrs=samples_df.shape
        self.N=int(N)
        self.k=k
        self.samples = np.array(samples_df.values)
        self.data = np.array(samples_df.drop(["风险"],axis=1).values)
        self.new_index=0

    def over_sampling(self):
        self.new_data =np.zeros([1, self.n_attrs])
        neighbors=NearestNeighbors(n_neighbors=self.k,n_jobs=2).fit(self.data)
        print("近邻",neighbors)
        for i in range(len(self.data)):
            # 最近的k个点
            nnarray=neighbors.kneighbors(self.data[i].reshape((1,-1)),return_distance=False)[0]
            self._populate2(i,nnarray)
        return self.new_data
    def _populate2(self,i,nnarray):
        for j in range(self.N):
            nn = random.randint(0,self.k-1)
            # 两个相近的点是否属于同类
            if self.samples[nnarray[nn]][0] == self.samples[i][0] and self.samples[i][0]==self.dtypes:
                dif = self.data[nnarray[nn]]-self.data[i]
                gap = random.random()
                d_np = self.data[i]+gap*dif
                d_np = np.insert(d_np,0,self.samples[i][0],axis=0)# 插入类型字段
                self.new_data=np.insert(self.new_data, self.new_index, d_np, axis=0)
                self.new_index += 1
                print(self.new_index)
            elif self.samples[i][0]!=self.dtypes or self.samples[nnarray[nn]][0] != self.samples[i][0] :
                d_np = self.data[i]
                d_np = np.insert(d_np, 0, self.samples[i][0], axis=0)  # 插入类型字段
                self.new_data = np.insert(self.new_data, self.new_index, d_np, axis=0)
                self.new_index += 1
                break