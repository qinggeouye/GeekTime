import copy


def lucky_draw_combination(n, m, result=None, all_results=None):
    """
    使用函数的递归（嵌套）调用，找出所有可能的中奖者的组合
    :param all_results: 中奖者的所有组合
    :param n: 参与抽奖的人
    :param result: 抽奖结果
    :param m: 中奖的人数
    :return: None
    """
    if result is None:
        result = []
    if all_results is None:
        all_results = []
    if len(result) == m:
        # print(result)
        return all_results.append(result)
    for i in range(len(n)):
        # 从剩下的人中，抽出一个人加入结果
        new_result = copy.copy(result)
        new_result.append(n[i])
        # 每人最多只能被抽中一次，当前被抽中的人之后的人，进入下一次抽奖
        rest_n = n[i + 1: len(n)]
        # 递归调用 在剩下的人中继续抽奖
        lucky_draw_combination(rest_n, m, new_result, all_results)
    return all_results


if __name__ == "__main__":
    total = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 被抽奖人列表
    m_ = [3, 2, 1]  # 三等奖、二等奖、一等奖的个数
    lucky1 = lucky_draw_combination(total, m_[0])
    for k1 in lucky1:
        total2 = copy.copy(total)
        for j1 in k1:
            total2.remove(j1)
        lucky2 = lucky_draw_combination(total2, m_[1])
        for k2 in lucky2:
            total3 = copy.copy(total2)
            for j2 in k2:
                total3.remove(j2)
            lucky3 = lucky_draw_combination(total3, m_[2])
            for k3 in lucky3:
                print(k1, k2, k3)
