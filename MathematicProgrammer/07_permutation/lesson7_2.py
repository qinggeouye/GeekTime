import copy

# 设置齐王的马跑完所需时间
q_horses_time = {"q1": 1.0, "q2": 2.0, "q3": 3.0}
# 设置田忌的马跑完所需时间
t_horses_time = {"t1": 1.5, "t2": 2.5, "t3": 3.5}
# 双方均随机选择出战的马匹

q_horses = ["q1", "q2", "q3"]
t_horses = ["t1", "t2", "t3"]


def permutation(horses, result=None, all_results=None):
    """
    使用函数的递归（嵌套）调用，找出所有可能的马匹出战顺序
    :param all_results: 马匹出战顺序的所有排列（全排列）
    :param horses: 目前还剩多少马没有出战
    :param result: 保存当前已经出战的马匹及顺序（其中一种排列）
    :return:
    """
    if result is None:
        result = []
    if all_results is None:
        all_results = []

    # 所有马匹都已经出战，返回出战顺序
    if len(horses) == 0:
        all_results.append(result)
        return

    for k in range(len(horses)):
        # 从剩下的未出战马匹中 选择一匹 加入结果
        new_result = copy.copy(result)
        new_result.append(horses[k])
        # 将已选择的马匹从未出战的列表中移除
        rest_horses = copy.copy(horses)
        rest_horses.pop(k)
        # 递归调用 对于剩余的马匹继续生成排列
        permutation(rest_horses, new_result, all_results)
    return all_results


def compare(t, q):
    t_won_cnt = 0
    for m in range(len(t)):
        print(str(t_horses_time.get(t[m])) + ',' + str(q_horses_time.get(q[m])))
        if t_horses_time.get(t[m]) < q_horses_time.get(q[m]):
            t_won_cnt = t_won_cnt + 1
    if t_won_cnt > len(t)//2:
        print("田忌获胜！")
    else:
        print("齐王获胜！")


if __name__ == '__main__':
    # 双方均随机安排马匹出战，田忌获胜的概率仍为 1/6
    t_results = permutation(t_horses)
    q_results = permutation(q_horses)
    print(t_results)
    print(q_results)
    for i in range(len(t_results)):
        for j in range(len(q_results)):
            compare(t_results[i], q_results[j])
