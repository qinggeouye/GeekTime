import numpy as np
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA

# 原始数据 包含了 3 个样本和 3 个特征，每一行表示一个样本，每一列表示一维特征
x = np.mat([[1, 3, -7], [2, 5, -14], [-3, -7, 2.0]])

# 矩阵按列进行标准化
x_s = scale(x, with_mean=True, with_std=True, axis=0)
print(" 标准化后的矩阵: \n", x_s)

# 计算协方差矩阵，注意这里要先进行转置，因为这里的函数是看行与行之间的协方差
x_cov = np.cov(x_s.transpose())  # numpy 中的协方差是除以 (m-1)
print(" 协方差矩阵: \n", x_cov, "\n")

# 求协方差矩阵的特征值和特征向量
eig_values, eig_vectors = np.linalg.eig(x_cov)
print(" 协方差矩阵的特征值: \n", eig_values)
print(" 协方差矩阵的特征向量(主成分): \n", eig_vectors, "\n")

# 找到最大的特征值 及其对应的特征向量
max_eig_val = -1
max_eig_val_index = -1

for i in range(0, eig_values.size):
    if eig_values[i] > max_eig_val:
        max_eig_val = eig_values[i]
        max_eig_val_index = i
    eig_vector_with_max_eig_val = eig_vectors[:, max_eig_val_index]

max_eig_val_index2 = np.argmax(eig_values)
max_eig_val2 = eig_values[max_eig_val_index2]
eig_vector_with_max_eig_val2 = eig_vectors[:, max_eig_val_index2]
print(" 最大的特征值: \n", max_eig_val2)
print(" 最大的特征值所对应的特征向量: \n", eig_vector_with_max_eig_val2)

# 输出最大的特征值 及其对应的特征向量 即第一额主成分
print(" 最大的特征值: \n", max_eig_val)
print(" 最大的特征值所对应的特征向量: \n", eig_vector_with_max_eig_val)

# 输出变换后的数据矩阵 注意，这里的三个值是表示三个样本，而特征值从 3 维变为 1 维
print(" 变换后的数据矩阵: \n", x_s.dot(eig_vector_with_max_eig_val), "\n")


"""
sklearn 库实现 PCA
"""
# 挑选前 2 个主成分
pca = PCA(n_components=2)
# 进行 PCA 分析
pca.fit(x_s)
# 输出变换后的数据矩阵 注意，这里的三个值是表示三个样本，而特征值从 3 维变为 1 维
print(" 方差（特征值）：\n", pca.explained_variance_)
print(" 主成分（特征向量）\n", pca.components_)
print(" 变换后的样本矩阵：\n", pca.transform(x_s))
print(" 信息量：\n", pca.explained_variance_ratio_)
# 它是各个主成分的方差所占的比例，表示第一个主成分包含了原始样本矩阵中的 98.27% 的信息，
# 而第二个主成分包含了原始样本矩阵中的 1.73% 的信息
