import pandas as pd
import numpy as np
from sklearn.preprocessing import scale
import time

"""
基于用户的协同过滤（第 38 讲））
数据集 MovieLens 
http://files.grouplens.org/datasets/movielens/ml-latest-small.zip
"""
# 运行开始时间
time_start = time.time()

# 加载用户对电影对评分数据
df = pd.read_csv("ml-latest-small/ratings.csv")

# 获取用户对数量和电影对数量
user_num = df["userId"].max()
movie_num = df["movieId"].max()

# 构造用户对电影的二元关系矩阵
user_rating = [[0.0] * movie_num for i in range(user_num)]

i = 0
# 获取每行的 index 和 row
for index, row in df.iterrows():
    # 由于用户和电影的 ID 都是从 1 开始，为了和 Python 的索引一致，减去 1
    userId = int(row["userId"]) - 1
    movieId = int(row["movieId"]) - 1

    # 设置用户对电影对评分
    user_rating[userId][movieId] = row["rating"]

    # 显示进度
    i += 1
    if i % 10000 == 0:
        print(i)

# 把二维数组转化为矩阵
x = np.mat(user_rating)
# print(x)


# 对每一行对数据，进行标准化
x_s = scale(x, with_mean=True, with_std=True, axis=1)
# print(" 标准化后对数据：", x_s)

# 获取 XX'
y = x_s.dot(x_s.transpose())
# print("XX' 的结果是：", y)

# 获用户相似度矩阵 US
us = [[0.0] * user_num for i in range(user_num)]
for userId1 in range(user_num):
    for userId2 in range(user_num):
        # 通过矩阵 Y 中的元素，计算夹角余弦
        us[userId1][userId2] = y[userId1][userId2] / np.sqrt((y[userId1][userId1] * y[userId2][userId2]))


# 通过用户之间的相似度，计算 USP 矩阵
usp = np.mat(us).dot(x_s)

# 求用于归一化的分母
usr = [0.0] * user_num
for userId in range(user_num):
    usr[userId] = sum(us[userId])

# 进行元素对应的除法 归一化
p = np.divide(usp, np.mat(usr).transpose())

# 运行结束时间
time_end = time.time()

print(p)
print(np.shape(p))

print("程序运行耗时：", time_end - time_start)
