import copy


def min_coins_recruit(target_money, coins):
    """
    对于总金额固定，使用函数的递归(嵌套调用)，找出最少钱币数
    :param target_money: 总金额大小
    :param coins: 可选面额的钱币列表，如 [2, 3, 7]
    :return:
    """
    if target_money == 0:
        return 0
    elif target_money < min(coins):
        return None  # 不存在或无解
    elif target_money in coins:
        return 1

    result = list()
    for j in coins:
        count = min_coins_recruit(target_money - j, coins)
        if count is None:
            continue
        else:
            result.append(count)
    if len(result) > 0:
        return min(result) + 1
    else:
        return None  # 不存在或无解


def min_coins_dyna_pro(target_money, coins):
    """
    对于总金额固定，使用动态规划算法，找出最少钱币数
    :param target_money: 总金额大小
    :param coins: 可选面额的钱币列表
    :return:
    """
    if min(coins) > target_money:
        return None
    # 每个额度的钱币数，初始化值为 None，假设不存在或无解
    count = list([None]*(target_money+1))
    # 一些确定额度的钱币数
    count[0] = 0
    for j in coins:
        if j <= target_money:
            count[j] = 1
    # 动态规划求解钱币数
    for i in range(min(coins) + 1, target_money+1):
        tmp_count = list()  # 临时保存钱币数
        tmp_coins = [j for j in coins if j <= i]  # 求解 count[i-j] 时，i-j 大于 0
        for j in tmp_coins:
            if count[i-j] is not None:
                tmp_count.append(count[i-j])
        if len(tmp_count) > 0:
            count[i] = min(tmp_count) + 1

    return count[target_money]


# 如何获取钱币组合？
if __name__ == "__main__":
    print("动态规划，最少钱币数：", min_coins_dyna_pro(50, [2, 3, 7]))
    print("递归方法，最少钱币数：", min_coins_recruit(50, [2, 3, 7]))
