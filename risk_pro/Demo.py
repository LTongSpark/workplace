import numpy as np

def num_nan(t):
    for i in range(t.shape[1]): #遍历每一列 t.shape[1] = 6
        temp_col = t[:,i]
        print(temp_col)
        nan_num = np.count_nonzero(np.isnan(temp_col))
        if nan_num != 0:
            temp_not_nan = temp_col[temp_col==temp_col]
            temp_col[np.isnan(temp_col)] = temp_not_nan.mean()
    return t


if __name__ == '__main__':
    t = np.arange(24).reshape((4,6)).astype("float")
    print(t)
    print("--------------------------")
    t[1,3:] = np.nan
    num_nan(t)
    print(t)

