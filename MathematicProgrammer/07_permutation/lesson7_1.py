import copy

# 设置齐王的马跑完所需时间
q_horses_time = {"q1": 1.0, "q2": 2.0, "q3": 3.0}
# 设置田忌的马跑完所需时间
t_horses_time = {"t1": 1.5, "t2": 2.5, "t3": 3.5}
# 在马匹跑完全程的时间上，这里 q1<t1<q2<t2<q3<t3 ，只有这样才能保证计算机得出和孙膑相同的结论

q_horses = ["q1", "q2", "q3"]
t_horses = ["t1", "t2", "t3"]


def permutation(horses, result=None):
    """
    使用函数的递归（嵌套）调用，找出所有可能的马匹出战顺序
    :param horses: 目前还剩多少马没有出战
    :param result: 保存当前已经出战的马匹及顺序
    :return:
    """
    if result is None:
        result = []

    # 所有马匹都已经出战，判断哪方获胜，输出结果
    if len(horses) == 0:
        print(result)
        compare(result, q_horses)
        return

    for i in range(len(horses)):
        # 从剩下的未出战马匹中 选择一匹 加入结果
        new_result = copy.copy(result)
        new_result.append(horses[i])
        # 将已选择的马匹从未出战的列表中移除
        rest_horses = copy.copy(horses)
        rest_horses.pop(i)
        # 递归调用 对于剩余的马匹继续生成排列
        permutation(rest_horses, new_result)


def compare(t, q):
    t_won_cnt = 0
    for i in range(len(t)):
        print(str(t_horses_time.get(t[i])) + ',' + str(q_horses_time.get(q[i])))
        if t_horses_time.get(t[i]) < q_horses_time.get(q[i]):
            t_won_cnt = t_won_cnt + 1
    if t_won_cnt > len(t)//2:
        print("田忌获胜！")
    else:
        print("齐王获胜！")


if __name__ == '__main__':
    # 如果田忌不听从孙膑的建议，而是随机安排马匹出战，那么他只有 1/6 的获胜概率
    permutation(t_horses)
