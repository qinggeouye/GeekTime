import queue
import random


class Node(object):
    def __init__(self, user_id):
        self.user_id = user_id
        self.friends = set()
        self.degree = 0


def set_user_relation(user_num, relation_num):
    """
    随机生成用户间的关系
    :param user_num: 用户数量 即节点的数量
    :param relation_num: 好友关系的数量 即边的数量
    :return:
    """
    # 生成所有表示用户的节点
    use_nodes = list([None] * user_num)
    for u in range(user_num):
        use_nodes[u] = Node(u)

    # 生成所有表示好友关系的边
    for r in range(relation_num):
        friend_a_id = random.randrange(user_num)
        friend_b_id = random.randrange(user_num)
        # 自己不能是自己的好友 如果生成的两个好友 id 相同，跳过
        if friend_a_id == friend_b_id:
            continue
        friend_a = use_nodes[friend_a_id]
        friend_b = use_nodes[friend_b_id]

        friend_a.friends.add(friend_b_id)
        friend_b.friends.add(friend_a_id)
    return use_nodes


def get_next_degree_friend(user_nodes, que, visited):
    """
    :param user_nodes: 用户节点网络
    :param que: 某一层用户节点 即第几度好友
    :param visited: 已访问的所有用户节点
    :return:
    """
    que_return = queue.Queue()  # 只保存某个用户的第几度好友
    visited_return = set()  # 保存从某个用户开始到第几度好友
    while not que.empty():
        current_user_id = que.get()
        if user_nodes[current_user_id] is None:
            continue
        for friend_id in user_nodes[current_user_id].friends:
            if user_nodes[friend_id] is None:
                continue
            if friend_id in visited:
                continue
            que_return.put(friend_id)
            visited_return.add(friend_id)  # 记录已经访问过的节点
    return que_return, visited_return


def has_overlap(visited_a, visited_b):
    # 两个 set() 的交集
    return len(visited_a & visited_b) > 0


def bi_bfs(user_nodes, user_id_a, user_id_b):
    """
    双向广度优先搜索 查找两人之间最短通路的长度
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

    que_a.put(user_id_a)  # 放入初始节点 a
    visited_a = set()  # 存放已经被访问的节点，防止回路
    visited_a.add(user_id_a)

    que_b.put(user_id_b)  # 放入初始节点 b
    visited_b = set()
    visited_b.add(user_id_b)

    # 设置 max_degree，防止两者之间不存在通路的情况
    degree_a, degree_b, max_degree = 0, 0, 20
    while degree_a + degree_b < max_degree:
        degree_a += 1
        # 沿着 a 出发的方向，继续广度优先搜索 degree+1 的好友
        que_a, visited_a = get_next_degree_friend(user_nodes, que_a, visited_a)
        # 判断到目前为止，被发现的 a 的好友，和被发现的 b 的好友，两个合集是否存在交集
        if has_overlap(visited_a, visited_b):
            return degree_a + degree_b

        degree_b += 1
        que_b, visited_b = get_next_degree_friend(user_nodes, que_b, visited_b)
        if has_overlap(visited_a, visited_b):
            return degree_a + degree_b
    # 广度优先搜索超过 max_degree 之后，仍然没有发现 a 和 b 的重叠，认为没有通路
    return -1


if __name__ == "__main__":
    user_nodes_list = set_user_relation(10, 20)
    for i in range(len(user_nodes_list)):
        print("用户 %s 的好友: %s" % (user_nodes_list[i].user_id, user_nodes_list[i].friends))
    print("---------双向广度优先搜索---------")
    print("两个用户节点之间的最短路径长度：", bi_bfs(user_nodes_list, 1, 2))
