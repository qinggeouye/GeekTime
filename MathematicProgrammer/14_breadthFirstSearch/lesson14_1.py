import queue


class Node(object):
    def __init__(self, user_id):
        self.user_id = user_id
        self.friends = set()
        self.degree = 0
        self.degrees = dict({user_id: 0})  # 从不同用户出发，到当前用户是第几度


def get_next_degree_friend(user_id, user_nodes, que, visited, degree):

    return que, visited


def has_overlap(visited_a, visited_b):

    return False


def bi_bfs(user_nodes, user_id_a, user_id_b):
    """
    双向广度优先搜索 查找两人之间最短通路到长度
    :param user_nodes: 所有用户节点
    :param user_id_a: 用户 a
    :param user_id_b: 用户 b
    :return:
    """
    # 防止数组越界
    if user_id_a > len(user_nodes) or user_id_b > len(user_nodes):
        return
    # 两个用户为同一人 返回0
    if user_id_a == user_id_b:
        return 0

    que_a = queue.Queue()  # 队列 a，用于从用户 a 出发的广度优先搜索
    que_b = queue.Queue()  # 队列 b，用于从用户 b 出发的广度优先搜索

    que_a.put(user_id_a)  # 放入初始节点
    visited_a = set()  # 存放已经被访问的节点，防止回路
    visited_a.add(user_id_a)

    que_b.put(user_id_b)
    visited_b = set()
    visited_b.add(user_id_b)

    # 设置 max_degree，防止两者之间不存在通路的情况
    degree_a, degree_b, max_degree = 0, 0, 20
    while degree_a + degree_b < max_degree:
        degree_a += 1
        # 沿着 a 出发的方向，继续广度优先搜索 degree+1 的好友
        que_a, visited_a = get_next_degree_friend(user_id_a, user_nodes, que_a, visited_a, degree_a)
        # 判断目前为止，被发现的 a 的好友，和被发现的 b 的好友，两个合集是否存在交集
        if has_overlap(visited_a, visited_b):
            return degree_a + degree_b
        degree_b += 1
        que_b, visited_b = get_next_degree_friend(user_id_b, user_nodes, que_b, visited_b, degree_b)
        if has_overlap(visited_a, visited_b):
            return degree_a + degree_b
    # 广度优先搜素超过 max_degree 之后，仍然没有发现 a 和 b 的重叠，认为没有通路
    return -1
