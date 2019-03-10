import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler, StandardScaler

"""
训练数据集的特征没有做 归一化/标准化 处理，没有转换到同一个可比较的范围，拟合效果较差
"""
# 读取 Boston Housing 中的 train.csv
df = pd.read_csv("/Users/qinggeouye/Desktop/GeekTime/MathematicProgrammer/29_featureTrans/train.csv")

# Dataframe 中除了最后一列 其余列都是特征，或者说变量
df_features = df.drop(['medv'], axis=1)
# Dataframe 最后一列是目标变量，或者说因变量
df_targets = df['medv']

# 使用特征和目标数据，拟合线性回归模型
regression = LinearRegression().fit(df_features, df_targets)
# 拟合程度的好坏
print(regression.score(df_features, df_targets))
# 各个特征所对应的系数
print(regression.coef_)


print("------------------------------归一化--------------------------------")
"""
归一化处理：x' = (x - min) / (max - min)
"""
# 基于 min 和 max 值的归一化
minMaxScaler = MinMaxScaler()

# 对原始数据进行归一化，包括特征值和目标变量
df_normalized = minMaxScaler.fit_transform(df.astype(dtype=float))
# 获取归一化之后的特征值
df_features_normalized = df_normalized[:, 0:-1]
# 获取归一化之后的目标值
df_targets_normalized = df_normalized[:, -1]

# 再次进行线性回归
regression_normalized = LinearRegression().fit(df_features_normalized, df_targets_normalized)
print(regression_normalized.score(df_features_normalized, df_targets_normalized))
print(regression_normalized.coef_)


print("------------------------------标准化--------------------------------")
"""
标准化处理：基于正太分布的 z 分数（z-score）标准化（Standardization），该方法假设数据呈标准正太分布。

x' = (x - u) / o

和归一化相比，z 分数这种标准化不易受到噪音数据的影响，并且保留了各维特征对目标函数的影响权重
"""

# 基于 Z 分数的标准化
standardScaler = StandardScaler()

standardScaler.fit(df.astype(dtype=float))
# 对原始数据进行标准化，包括特征值和目标变量
df_standardized = standardScaler.transform(df.astype(dtype=float))

# 获取标准化之后的特征值
df_features_standardized = df_standardized[:, 0:-1]
# 获取标准化之后的目标值
df_targets_standardized = df_standardized[:, -1]

# 再次进行线性回归
regression_standardized = LinearRegression().fit(df_features_standardized, df_targets_standardized)
print(regression_standardized.score(df_features_standardized, df_targets_standardized))
print(regression_standardized.coef_)


print("------------------------------测试集--------------------------------")
"""
测试数据集 test.csv
测试数据的目标值 submission_example.csv
"""
df_test = pd.read_csv("/Users/qinggeouye/Desktop/GeekTime/MathematicProgrammer/29_featureTrans/test.csv")
expected_test = pd.read_csv("/Users/qinggeouye/Desktop/GeekTime/MathematicProgrammer/29_featureTrans"
                            "/submission_example.csv")['medv']

# 归一化 预测结果
minMaxScaler_test = MinMaxScaler()
df_test_normalized = minMaxScaler_test.fit_transform(df_test.astype(dtype=float))
df_test_features_normalized = df_test_normalized[:, :]
predicted_normalized = regression_normalized.predict(df_test_features_normalized)
print("归一化预测结果与实际值的均方根误差：%s" % np.sqrt(np.mean((predicted_normalized - expected_test) ** 2)))

# 标准化 预测结果
standardScaler_test = StandardScaler()
standardScaler_test.fit(df_test.astype(dtype=float))
df_test_standardized = standardScaler_test.transform(df_test.astype(dtype=float))
df_test_features_standardized = df_test_standardized[:, :]
predicted_standardized = regression_standardized.predict(df_test_features_standardized)
print("标准化预测结果与实际值的均方根误差：%s" % np.sqrt(np.mean((predicted_standardized - expected_test) ** 2)))
