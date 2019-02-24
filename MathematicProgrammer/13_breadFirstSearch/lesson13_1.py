import random
import queue


class Node(object):
    def __init__(self, user_id):
        self.user_id = user_id   # 用户 id ，作为节点的名称
        self.friends = set()  # 存放相连的朋友节点，set 自动去重
        self.degree = 0  # 用于存放和给定的用户节点，是几度好友关系


def set_user_relation(user_num, relation_num):
    """
    随机生成用户间的关系
    :param user_num: 用户数量 即节点的数量
    :param relation_num: 好友关系的数量 即边的数量
    :return:
    """
    # 生成所有表示用户的节点
    use_nodes = list([None]*user_num)
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


def bfs(user_nodes, user_id):
    """
    广度优先搜索 查找好友
    :param user_nodes: 用户的节点
    :param user_id: 给定的用户 id ，给该用户查找好友
    :return:
    """
    # 防止数组越界
    if user_id > len(user_nodes):
        return

    que = queue.Queue()
    que.put(user_id)  # 放入初始节点
    visited = set()  # 存放已经访问过的节点 防止回路
    visited.add(user_id)

    while not que.empty():
        current_user_id = que.get()  # 拿出队列头部第一个节点
        if user_nodes[current_user_id] is None:
            continue
        # 遍历刚刚拿出的这个节点的所有直接链接节点 并加入队列尾部
        for friend_id in user_nodes[current_user_id].friends:
            if user_nodes[friend_id] is None:
                continue
            if friend_id in visited:
                continue
            que.put(friend_id)
            visited.add(friend_id)  # 记录已经访问过的节点
            # 好友度数是当前节点的好友度数加 1
            user_nodes[friend_id].degree = user_nodes[current_user_id].degree + 1
            print("\t用户 %s 的 %s 度好友：%s" % (user_id, user_nodes[friend_id].degree, friend_id))


if __name__ == "__main__":
    user_nodes_list = set_user_relation(10, 20)
    for i in range(len(user_nodes_list)):
        print("用户 %s 的好友: %s" % (user_nodes_list[i].user_id, user_nodes_list[i].friends))
    print("---------广度优先搜索---------")
    bfs(user_nodes_list, 1)
