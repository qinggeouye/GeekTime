import numpy as np

people_type = np.dtype({'names': ['name', 'chinese', 'math', 'english', 'total'],
                        'formats': ['S32', 'i', 'i', 'f', 'f']})
peoples = np.array([('ZhangFei', 60, 65, 30, 0), ('GuanYu', 95, 85, 98, 0),
                    ('ZhaoYun', 93, 92, 96, 0), ('HuangZhong', 90, 88, 77, 0),
                    ('DianWei', 80, 90, 90, 0)], dtype=people_type)

chinese = peoples[:]['chinese']
math = peoples[:]['math']
english = peoples[:]['english']

peoples[:]['total'] = chinese + math + english
print("rank of total scores is \n %s" % np.sort(peoples, order='total'))
print("\n")
print("rank of total scores is \n %s" % np.sort(chinese + math + english))
print("\n")

for key in list(people_type.fields.keys())[1:4]:
    print("mean of %s is %s" % (key, np.mean(peoples[:][key])))
    print("max of %s is %s" % (key, np.amax(peoples[:][key])))
    print("min of %s is %s" % (key, np.amin(peoples[:][key])))
    print("std of %s is %s" % (key, np.std(peoples[:][key])))
    print("var of %s is %s" % (key, np.var(peoples[:][key])))
    print("\n")
