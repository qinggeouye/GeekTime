import pandas as pd
import numpy as np
from sklearn.preprocessing import scale
import time

# 运行开始时间
time_start = time.time()

# 加载用户对电影对评分数据
df_ratings = pd.read_csv("ml-latest-small/ratings.csv")

# 获取用户对数量和电影对数量 这里只取前 1/10 , 减少数据规模
user_num = int(df_ratings["userId"].max() / 2)
movie_num = int(df_ratings["movieId"].max() / 2)
print(user_num, movie_num)
df_ratings = df_ratings[df_ratings["userId"] <= user_num]
df_ratings = df_ratings[df_ratings["movieId"] <= movie_num]

# 构造用户对电影对二元关系矩阵
user_rating = np.zeros((user_num, movie_num))

# 由于用户和电影对 ID 都是从 1 开始，为了和 Python 的索引一致，减去 1
df_ratings["userId"] = df_ratings["userId"] - 1
df_ratings["movieId"] = df_ratings["movieId"] - 1
# 设置用户对电影对评分
for userId in range(user_num):
    user_rating[userId][df_ratings[df_ratings["userId"] == userId]["movieId"]] = \
        df_ratings[df_ratings["userId"] == userId]["rating"]

# 二维数组转化为矩阵
x = np.mat(user_rating)

# 标准化每位用户的评分数据 每一行
x_s = scale(x, with_mean=True, with_std=True, axis=1)

# 进行 SVD 奇异值分解
u, sigma, vt = np.linalg.svd(x_s, full_matrices=False, compute_uv=True)
# print("U 矩阵：", u)
print("Sigma 奇异值：", sigma)
# print("V 矩阵：", vt)

# 加载电影元信息
df_movies = pd.read_csv("ml-latest-small/movies.csv")
dict_movies = dict(zip(df_movies["movieId"], df_movies["title"] + ", " + df_movies["genres"]))
# print(dict_movies)

# 输出和某个奇异值高度相关的电影 这些电影代表了一个主题
# (注意：向量中电影的 ID 和原始的电影的 ID 相差 1，所以在读取 dict_movies 需要使用 i+1)
print(np.max(vt[1, :]))
print(list(zip(np.where(vt[1] > 0.1)[0] + 1, vt[1][np.where(vt[1] > 0.1)],
               [dict_movies[i] for i in (np.where(vt[1] > 0.1)[0] + 1)])))

# 运行结束时间
time_end = time.time()
print("程序运行耗时：", time_end - time_start)
