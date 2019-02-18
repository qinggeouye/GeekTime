def get_str_distance(a, b):
    """
    使用状态转移方程，计算两个字符串之间的编辑距离
    :param a: 第一个字符串
    :param b: 第二个字符串
    :return: 两者之间的编辑距离
    """
    if a is None or b is None:
        return -1
    # 初始化 用于记录状态转移的二维表 , d 中 0 下标位置对应表示空串
    d = [[0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]
    # 如果 i 为 0 ，且 j 大于等于 0 ，那么 d[i][j] 为 j
    d[0][:] = [j for j in range(len(b) + 1)]
    # 如果 i 大于等于 0 ，且 j 为 0 ，那么 d[i][j] 为 i
    for i in range(len(a) + 1):
        d[i][0] = i

    # 实现状态转移方程
    # 注意，代码里的状态转移是从 d[i][j] 到 d[i+1][j+1] ，而不是从 d[i-1][j-1] 到 d[i][j]，本质上是一样的
    for i in range(len(a)):
        for j in range(len(b)):
            r = 0
            if a[i] != b[j]:
                r = 1
            first_append = d[i][j+1] + 1
            second_append = d[i+1][j] + 1
            replace = d[i][j] + r

            min_d = min(first_append, second_append, replace)
            d[i+1][j+1] = min_d

    return d[len(a)][len(b)]


if __name__ == "__main__":
    print(get_str_distance("mouse", "mouuuse"))
