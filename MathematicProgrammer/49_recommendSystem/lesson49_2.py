import numpy as np
import pandas as pd
from sklearn.preprocessing import scale
import time

"""
对 lesson49_1.py 优化：矩阵操作
"""
# 运行开始时间
time_start = time.time()

# 加载用户对电影对评分数据
df = pd.read_csv("ml-latest-small/ratings.csv")

# 获取用户对数量和电影对数量
user_num = df["userId"].max()
movie_num = df["movieId"].max()

# 构造用户对电影的二元关系矩阵
user_rating = np.zeros((user_num, movie_num))
# 由于用户和电影的 ID 都是从 1 开始，为了和 Python 的索引一致，减去 1
df["userId"] = df["userId"] - 1
df["movieId"] = df["movieId"] - 1
for index in range(user_num):
    user_rating[index][df[df["userId"] == index]["movieId"]] = df[df["userId"] == index]["rating"]

# 把二维数组转化为矩阵
x = np.mat(user_rating)
# 对每一行对数据，进行标准化
x_s = scale(x, with_mean=True, with_std=True, axis=1)

# 获取 XX'
y = x_s.dot(x_s.transpose())
# 夹角余弦的分母
v = np.zeros((np.shape(y)[0], np.shape(y)[1]))
v[:] = np.diag(y)
# 获用户相似度矩阵 US , 对应位置上元素相除
us = y/v

# 通过用户之间的相似度，计算 USP 矩阵
usp = np.mat(us).dot(x_s)

# 求用于归一化的分母 按行求和
usr = np.sum(us, axis=1)

# 进行元素对应的除法 归一化
p = np.divide(usp, np.mat(usr).transpose())

# 运行结束时间
time_end = time.time()

print(p)
print(np.shape(p))

print("程序运行耗时：", time_end - time_start)
