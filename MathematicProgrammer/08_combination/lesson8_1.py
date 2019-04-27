import copy


def combine(teams, result, m):
    """
    使用函数的递归（嵌套）调用，找出所有可能的队伍组合
    :param teams: 目前还剩多少队伍没有参与组合
    :param result: 保存当前已经组合的队伍
    :param m: 每个组合的队伍个数
    :return:
    """
    # 挑选完 m 个元素 输出结果
    if len(result) == m:
        print(result)
        return

    for i, team in enumerate(teams):
        # 从剩下的队伍中 选择一个 加入结果
        new_result = copy.copy(result)
        new_result.append(team)
        # 只考虑当前选择之后的所有队伍(组合与排列的区别)
        rest_teams = teams[i+1:len(teams)]
        # 递归调用 对于剩余的队伍继续生成组合
        combine(rest_teams, new_result, m)


# 从 3 个元素中选择 2 个元素的所有组合
if __name__ == "__main__":
    teams_ = list(["t1", "t2", "t3"])
    combine(teams_, [], 2)
