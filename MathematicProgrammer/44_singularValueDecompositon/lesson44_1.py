import numpy as np
from numpy import linalg as la

"""
实现奇异值分解 SVD Singular Value Decomposition
潜在语义分析模型 LSA Latent Semantic Analysis
"""

# 文档集合 文档和词条关系矩阵 行表示文档 列表示词条
x = np.mat([[1, 1, 1, 0, 0], [2, 2, 2, 0, 0],
            [1, 1, 1, 0, 0], [5, 5, 5, 0, 0],
            [0, 0, 0, 2, 2], [0, 0, 0, 3, 3],
            [0, 0, 0, 1, 1]])


# 对 文档-词条 矩阵，进行 SCD 分解

# 左奇异向量 XX' -> U
u_eig_values, u_eig_vectors = np.linalg.eig(x.dot(x.transpose()))
u_eig_vectors = u_eig_vectors[:, np.argsort(u_eig_values)[::-1]]  # 降序排序
u_eig_values = np.sort(u_eig_values)[::-1]  # 降序排序
# u_eig_values = u_eig_values[u_eig_values > 1e-5]
print(" 特征值：", np.around(u_eig_values, decimals=4))
print(" 左奇异向量: \n", np.around(u_eig_vectors, decimals=2), "\n")

# 右奇异向量 X'X -> V
v_eig_values, v_eig_vectors = np.linalg.eig(x.transpose().dot(x))
v_eig_vectors = v_eig_vectors[:, np.argsort(v_eig_values)[::-1]]  # 降序排序
v_eig_values = np.sort(v_eig_values)[::-1]  # 降序排序
# v_eig_values = v_eig_values[v_eig_values > 1e-5]
print(" 特征值：", np.around(v_eig_values, decimals=4))
print(" 右奇异向量: \n", np.around(v_eig_vectors, decimals=2), "\n")


# 奇异值矩阵 S , 对角线非零元素 奇异值 σ

# 因为 矩阵XX' 与 矩阵X'X 的特征多项式相同，所以特征值相同（X' 是 X 的转置）
# 特征值的求法-> |XX' - λI| = |(XX'-λI)'| = |X'X - λI| = 0
# 因为 XX' = (USV')(VS'U') = U(SS')U' , 则奇异值 σ 是 XX' 非零特征值的平方根
s_eig_values = np.sqrt(u_eig_values[u_eig_values > 0])
print(" 奇异值: ", np.around(s_eig_values, decimals=4))
s_eig_values2 = np.sqrt(v_eig_values[v_eig_values > 0])
print(" 奇异值: ", np.around(s_eig_values2, decimals=4), "\n")
S = np.zeros((7, 5))  # 奇异矩阵
for i in range(len(s_eig_values)):
    S[i, i] = s_eig_values[i]
print(" 酉矩阵: \n", u_eig_vectors.transpose().dot(u_eig_vectors))  # 酉矩阵
print(" 酉矩阵: \n", v_eig_vectors.transpose().dot(v_eig_vectors))  # 酉矩阵
print(" 矩阵还原: \n", u_eig_vectors.dot(S).dot(v_eig_vectors.transpose()))


print("\n--------------- numpy 库的 linalg 已经实现 SVD ---------------\n")
# linalg 已经实现 SVD
U, sigma, VT = la.svd(x)
print(U, "\n")
print(sigma, "\n")
print(VT, "\n")  # 注意 VT 已经转置
S2 = np.zeros((7, 5))  # 奇异矩阵
for i in range(len(sigma)):
    S2[i, i] = sigma[i]
print(" 酉矩阵: \n", U.transpose().dot(U))  # 酉矩阵
print(" 酉矩阵: \n", VT.transpose().dot(VT))  # 酉矩阵
print(" 矩阵还原: \n", U.dot(S2).dot(VT))

