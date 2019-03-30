import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

"""
使用 numpy 矩阵操作实现最小二乘法
"""
x = np.mat([[0, 1], [1, -1], [2, 8]])
y = np.mat([[1.4], [-0.48], [13.2]])

# 分别求出矩阵 X' 、X'X 、(X'X) 的逆
# 注意，这里的 I 表示逆矩阵而不是单位矩阵
print("X 矩阵的转置 X': \n", x.transpose())
print("\nX' 点乘 X: \n", x.transpose().dot(x))
print("\nX'X 矩阵的逆\n", (x.transpose().dot(x)).I)

print("\nX'X 矩阵的逆点乘 X'\n", (x.transpose().dot(x)).I.dot(x.transpose()))
print("\n 系数矩阵 B: \n", (x.transpose().dot(x)).I.dot(x.transpose()).dot(y))

# 考虑截距
x = np.mat([[1, 0, 1], [1, 1, -1], [1, 2, 8]])
print("\n 系数矩阵 B: \n", (x.transpose().dot(x)).I.dot(x.transpose()).dot(y))

print("\n-----------------sklearn 库中的 LinearRegression().fit()----------------\n")

"""
sklearn 库中的 LinearRegression().fit() 函数求解
"""
df = pd.read_csv("./test.csv")
# Dataframe 中除了最后一列，其余列都是特征（自变量）
df_features = df.drop(['y'], axis=1)
# Dataframe 中最后一列是目标变量（因变量）
df_targets = df['y']

print(df_features, df_targets)
print("\n")
# 使用特征和目标函数拟合线性回归模型
regression = LinearRegression().fit(df_features, df_targets)
# 拟合程度的好坏
print(regression.score(df_features, df_targets), "\n")
print(regression.intercept_, "\n")
# 各个特征对应的系数
print(regression.coef_, "\n")


print("\n----------------- 思考题 ----------------\n")
"""
思考题
"""
x = np.mat([[1, 3, -7], [2, 5, 4], [-3, -7, -2], [1, 4, -12]])
y = np.mat([[-7.5], [5.2], [-7.5], [-15]])
print("\n 系数矩阵 B: \n", (x.transpose().dot(x)).I.dot(x.transpose()).dot(y))
