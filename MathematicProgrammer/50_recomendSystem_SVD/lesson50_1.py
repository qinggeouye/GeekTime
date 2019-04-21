import pandas as pd
import numpy as np
from sklearn.preprocessing import scale

# 加载用户对电影的评分数据
df_ratings = pd.read_csv("ml-latest-small/ratings.csv")

# 获取用户的数量和电影的数量，这里我们只取前 1/10 来减小数据规模
user_num = int(df_ratings["userId"].max() / 10)
movie_num = int(df_ratings["movieId"].max() / 10)
print(user_num, movie_num)

# 构造用户对电影的二元关系矩阵
user_rating = [[0.0] * movie_num for i in range(user_num)]

for index, row in df_ratings.iterrows():  # 获取每行的 index、row
    # 由于用户和电影的 ID 都是从 1 开始，为了和 Python 的索引一致，减去 1
    userId = int(row["userId"]) - 1
    movieId = int(row["movieId"]) - 1

    # 我们只取前 1/10 来减小数据规模
    if (userId >= user_num) or (movieId >= movie_num):
        continue

    # 设置用户对电影的评分
    user_rating[userId][movieId] = row["rating"]

# 把二维数组转化为矩阵
x = np.mat(user_rating)

# 对每一行的数据，进行标准化
x_s = scale(x, with_mean=True, with_std=True, axis=1)

u, sigma, vt = np.linalg.svd(x_s, full_matrices=False, compute_uv=True)
print("U 矩阵：", u)
print("Sigma 奇异值：", sigma)
print("V 矩阵：", vt)

# 加载电影元信息
df_movies = pd.read_csv("ml-latest-small/movies.csv")
dict_movies = dict()
for index, row in df_movies.iterrows():
    dict_movies[row["movieId"]] = "{0}, {1}".format(row["title"], row["genres"])
print(dict_movies)

# 输出和某个奇异值高度相关的电影，这些电影代表了一个主题
# (注意：向量中电影的 ID 和原始的电影的 ID 相差 1，所以在读取 dict_movies 需要使用 i+1)
print(np.max(vt[1,:]))
for i in range(movie_num):
    if (vt[1][i] > 0.1):
        print(i + 1, vt[1][i], dict_movies[i + 1])
