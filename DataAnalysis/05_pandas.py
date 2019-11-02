import numpy as np
import pandas as pd

scores = pd.DataFrame(
    {'姓名': ['张飞', '关羽', '赵云', '黄忠', '典韦', '典韦'], '语文': [66, 95, 95, 90, 80, 80], '英语': [65, 85, 92, 88, 90, 90],
     '数学': [np.NaN, 98, 96, 77, 90, 90], })

print(scores)

# 查找空值所在的列
isNaN = scores.isna().any()  # isnull(), isnull().any()
isNaN = isNaN[isNaN == True]
print(scores[isNaN.index])

# 列的平均值填充空值
for col in isNaN.index:
    scores[col].fillna(scores[col].mean(), inplace=True)
print(scores)

# 去除不必要的行（空值）
# scores = scores.drop(index=[0])
# scores = scores.dropna()

# 去除重复行
scores = scores.drop_duplicates()
print(scores)

# 新增一列'总和'
# scores['总和'] = scores['语文'] + scores['数学'] + scores['英语']
scores['总和'] = scores.sum(axis=1)
print(scores)
