import numpy as np


def adj_init(alpha, n, adj_list):
    """
    跳转概率、邻接矩阵 adj、初始化 PageRank 的值
    :param adj_list: 用于构建邻接矩阵
    :param alpha: 随机跳转概率的 alpha
    :param n: 网页节点数
    :return:
    """

    # 初始化随机跳转概率的矩阵（ 2行1列 ）
    jump = np.full([2, 1], [[alpha], [1 - alpha]], dtype=float)

    # 邻接矩阵的构建（ N行N列的矩阵，第 i 行第 j 列表示从节点 i 到节点 j 是否存在连接，0否1是）
    adj = np.full([n, n], adj_list, dtype=float)
    # 对邻接矩阵归一化
    row_sums = adj.sum(axis=1)  # 对每一行求和
    row_sums[row_sums == 0] = 0.1  # 防止由于分母出现 0 而导致的 Nan
    adj = adj / row_sums[:, np.newaxis]  # 除以每行之和的归一化

    # 初始的 PageRank 值，通常是设置所有值为 1.0 （1行N列）
    pr = np.full([1, n], 1, dtype=float)

    return jump, adj, pr


def page_rank(jump, adj, pr, max_try, delta_threshold):
    """

    :param jump: 跳转概率[[alpha], [1 - alpha]]
    :param adj: 邻接矩阵
    :param pr: 初始的 Page Rank 值
    :param max_try: 最大迭代次数
    :param delta_threshold: 误差的阈值
    :return:
    """
    # PageRank 算法本身是迭代方式进行的，当最终的取值趋于稳定后结束
    for i in range(0, max_try):
        # 保存前一次的 PageRank 数值
        pr_tmp = pr

        # 进行点乘，计算求和(PR(pj)/L(Pj))
        pr = np.dot(pr, adj)

        n = len(adj)  # 节点个数
        # 转置保存 求和(PR(pj)/L(Pj)) 结果的矩阵，并增加长度为 n 的列向量，其中每个元素的值为 1/n
        pr_jump = np.full([n, 2], [[0, 1 / n]])
        pr_jump[:, :-1] = pr.transpose()

        # 进行点乘，计算 alpha(求和(PR(pj)/L(Pj))) + (1-alpha)/n
        pr = np.dot(pr_jump, jump)

        # 归一化 PageRank 得分
        pr = pr.transpose()  # 转为行向量
        pr = pr / pr.sum()

        print("round", i + 1, pr)

        # 思考题
        # 计算前后两次的 PageRank 数值的误差，判断是否需要结束迭代
        delta = list(map(abs, (pr/pr_tmp)))
        delta = abs(np.max(delta) - 1)  # 最大误差的百分比
        if delta <= delta_threshold:
            return pr
        else:
            continue

    return -1


if __name__ == "__main__":
    adj_list_ = [[0, 0, 1, 0, 0], [1, 0, 1, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0]]
    jump_, adj_, pr_ = adj_init(0.9, 5, adj_list_)
    maxTry_ = 20
    deltaThreshold_ = 0.00001
    page_rank(jump_, adj_, pr_, maxTry_, deltaThreshold_)
