import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import scipy.stats as ss

"""
显著性检验：方差分析（Analysis of Variance，ANOVA，F 检验）
随机性：样本是随机采样但
独立性：来自不同组但样本是相互独立但
正太分布性：组内样本都来自一个正太分布
方差齐性：不同组但方差相等或相近
"""

# 读取数据， d1 对应于算法 a，d2 对应于算法 b
df = pd.read_csv("./oneway.csv")
d1 = df[df['algo'] == 'a']['ratio']
d2 = df[df['algo'] == 'b']['ratio']

# 检验两个水平的正态性
print('---------------- 检验两个水平的正态性 ----------------')
print(ss.normaltest(d1))
print(ss.normaltest(d2))

# 检测两个水平的方差齐性
print('---------------- 检测两个水平的方差齐性 ----------------')
args = [d1, d2]
print(ss.levene(*args))

# F 检验的第一种方法
print('---------------- F 检验的第一种方法 ----------------')
print(ss.f_oneway(*args))

# F 检验的第二种方法
print('---------------- F 检验的第二种方法 ----------------')
model = ols('ratio ~ algo', df).fit()
anovat = anova_lm(model)
print(anovat)
