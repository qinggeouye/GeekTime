import pandas as pd

# 读取数据
data_init = pd.read_csv("./11_clothingStoreMembers.csv")
print(data_init)
print(type(data_init))

# 清洗数据

# 删除 '\t' 列, 读取 csv 文件多了一列
data_init.drop(columns='\t', inplace=True)
print(data_init)
# 重命名列名
data_init.rename(
    columns={"0": "SEQ", "1": "NAME", "2": "AGE", "3": "WEIGHT", "4": "BUST_M", "5": "WAIST_M", "6": "HIP_M",
             "7": "BUST_F", "8": "WAIST_F", "9": "HIP_F"}, inplace=True)
print(data_init)

# 1、完整性
# 删除空行
data_init.dropna(how='all', inplace=True)
print(data_init)

# 4、唯一性
# 一列多个参数切分
data_init[["FIRST_NAME", "LAST_NAME"]] = data_init["NAME"].str.split(expand=True)
data_init.drop("NAME", axis=1, inplace=True)
print(data_init)
# 删除重复数据
data_init.drop_duplicates(["FIRST_NAME", "LAST_NAME"], inplace=True)
print(data_init)

# 2、全面性
# 列数据单位统一, 体重 WEIGHT 单位统一（lbs 英镑， kg 千克）
rows_with_lbs = data_init["WEIGHT"].str.contains("lbs").fillna(False)
print(rows_with_lbs)
# lbs 转为 kg
for i, lbs_row in data_init[rows_with_lbs].iterrows():
    weight = int(float(lbs_row["WEIGHT"][:-3]) / 2.2)
    data_init.at[i, "WEIGHT"] = "{}kgs".format(weight)
print(data_init)

# 3、合理性
# 非 ASCII 字符转换，这里删除处理
data_init["FIRST_NAME"].replace({r'[^\x00-\x7F]+': ''}, regex=True, inplace=True)
data_init["LAST_NAME"].replace({r'[^\x00-\x7F]+': ''}, regex=True, inplace=True)
print(data_init)

# 1、完整性
# 补充缺失值-均值补充
data_init["AGE"].fillna(data_init["AGE"].mean(), inplace=True)
# 体重先去掉 kgs 的单位符号
data_init["WEIGHT"].replace('kgs$', '', regex=True, inplace=True)  # 不带单位符号 kgs
data_init["WEIGHT"] = data_init["WEIGHT"].astype('float')
data_init["WEIGHT"].fillna(data_init["WEIGHT"].mean(), inplace=True)

data_init.replace('-', 0, regex=True, inplace=True)  # 读取的 csv 数据多了'-'
data_init["WAIST_F"] = data_init["WAIST_F"].astype('float')
data_init["WAIST_F"].fillna(data_init["WAIST_F"].mean(), inplace=True)
print(data_init)

# 用最高频的数据填充
age_max_freq = data_init["AGE"].value_counts().index[0]
print(age_max_freq)
data_init["AGE"].fillna(age_max_freq, inplace=True)
print(data_init)
