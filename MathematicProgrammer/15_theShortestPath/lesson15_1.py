import random


class Node(object):
    def __init__(self, user_id):
        self.user_id = user_id  # 用户节点 id
        self.friends = list()  # 用户指向的节点，元素表示节点 id
        self.weights = list()  # 用户指向的节点，其边的权重值


def set_user_relation(user_num, relation_num):
    """
    随机生成用户间的关系
    :param user_num: 用户数量 即节点的数量
    :param relation_num: 好友关系的数量 即边的数量
    :return:
    """
    # 生成所有表示用户的节点
    use_nodes = list()
    for u in range(user_num):
        use_nodes.append(Node(u))

    # 生成所有表示好友关系的边
    for r in range(relation_num):
        friend_a_id = random.randrange(user_num)
        friend_b_id = random.randrange(user_num)
        # 自己不能是自己的好友 如果生成的两个好友 id 相同，跳过
        if friend_a_id == friend_b_id or friend_b_id in use_nodes[friend_a_id].friends:
            continue
        friend_a = use_nodes[friend_a_id]
        friend_a.friends.append(friend_b_id)  # 用户 friend_a 的好友
        friend_a.weights.append(round(random.random(), 2))  # 权重值
    return use_nodes


def dijkstra(graph, source):
    """
    Dijkstra 单源最短路径算法简单实现
    :param graph: 图
    :param source: 源点（起始点）
    :return: pre_node 前驱节点
    """
    nodes_list = list()
    # 图 graph 中的节点id的集合
    for node in range(len(graph)):
        nodes_list.append(graph[node].user_id)

    # 保存了从起始点 source 到任意节点到最小权重值（最短路径大小）
    min_weights_list = list([float("Inf")] * len(graph))  # 无穷大 Inf , 下标与节点对应
    # 从源点 source 出发，已经找到 最小权重值（最短路径值大小）的节点集合
    found_nodes = list()  # 元素表示节点 id
    # 前驱节点
    pre_node = list([None] * len(graph))  # 下标与节点对应，其元素为下标对应的前驱节点

    # 初始的时候
    if len(graph[source].friends) == 0:
        return pre_node
    for node in range(len(graph[source].friends)):
        min_weights_list[graph[source].friends[node]] = graph[source].weights[node]
        # 初始，与源点 source 直连的节点，其前驱节点为 source
        pre_node[graph[source].friends[node]] = source
    # min_weights_list[source] = 0  # 去掉这一步，便于查找最小权重值
    found_nodes.append(source)

    while len(set(nodes_list) - set(found_nodes)) != 0:
        # 图可能是不连通，min_weights_list 中, 源点 source 到某些节点的权重值无穷大
        if min(min_weights_list) == float("Inf"):
            break

        # 第一步 查找最小权重值的节点
        min_weight_index = min_weights_list.index(min(min_weights_list))  # 下标对应节点的id
        found_nodes.append(min_weight_index)

        # 第二步 更新权重值
        for node in range(len(graph[min_weight_index].friends)):
            # 已经找到最短路径的节点，不再更新
            if graph[min_weight_index].friends[node] in found_nodes:
                continue
            if min_weights_list[min_weight_index] + graph[min_weight_index].weights[node] < \
                    min_weights_list[graph[min_weight_index].friends[node]]:
                # 更新 min_weights_list 中节点的权重值
                min_weights_list[graph[min_weight_index].friends[node]] = min_weights_list[min_weight_index] + \
                                                                          graph[min_weight_index].weights[node]
                # 更新前驱节点
                pre_node[graph[min_weight_index].friends[node]] = min_weight_index
        # 该点权重值置为无穷大，为下一次循环准备
        min_weights_list[min_weight_index] = float("Inf")

    return pre_node


def shortest_path(graph, source, pre_node):
    """
    打印源点 source 到其它节点到最短路径
    :param graph: 图
    :param source: 源点
    :param pre_node: 前驱节点列表
    :return:
    """
    print("-------------- 源点 %s 到其它各节点的最短路径 ------------" % source)
    for k in range(len(graph)):
        pre = pre_node[k]
        if pre is None:
            print("源点 %s 到 %s 的最短路径：不存在" % (source, k))
            continue
        path = [str(k)]
        while pre != source and pre is not None:
            path.append(" -> ")
            path.append(str(pre))
            pre = pre_node[pre]
        if pre == source:
            path.append(" -> ")
            path.append(str(pre))
        print("源点 %s 到 %s 的最短路径：%s" % (source, k, ''.join(path[::-1])))


if __name__ == "__main__":
    user_nodes_list = set_user_relation(10, 20)
    for i in range(len(user_nodes_list)):
        if len(user_nodes_list[i].friends):
            print("用户 {} 的好友: {}, \t权重值 {}".format(user_nodes_list[i].user_id, user_nodes_list[i].friends,
                                                   user_nodes_list[i].weights))
        else:
            print("用户 {} 的好友: 不存在".format(user_nodes_list[i].user_id))
    print("\n------------- Dijkstra 单源最短路径算法 --------------\n")
    s = 1  # 源点
    pre_node_list = dijkstra(user_nodes_list, s)
    print("下标节点对应的前驱节点：", pre_node_list, "\n")
    # 打印路径
    shortest_path(user_nodes_list, s, pre_node_list)
