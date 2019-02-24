class TreeNode(object):
    """
    前缀树的节点
    """
    def __init__(self, label=None, prefix=None, explanation=None, is_word=False):
        """
        初始化节点
        :param label: 节点的名称 在前缀树里是单个字母
        :param prefix: 从树的根节点到当前节点这条通路上，全部字母所组成的前缀。
        如，通路 b->o->y，对于字母 o，前缀是 b；对于字母 y，前缀是 bo
        :param explanation: 单词解释
        :param is_word: 判断是不是一个单词 ，False 不是
        """
        self.explanation = explanation
        self.prefix = prefix
        self.label = label
        self.is_word = is_word
        self.sons = dict()  # 存放子节点


class Tree(object):
    def __init__(self):
        self._root = TreeNode()

    def add(self, word, explanation):
        """
        向 Tree 中添加一个单词
        :param explanation: 单词解释
        :param word: 英文单词
        :return:
        """
        cur = self._root  # 从根节点开始
        for c in word:  # 遍历单词中的字母
            if cur.sons.get(c, None) is None:
                if cur.prefix is None:
                    prefix = cur.label
                else:
                    prefix = cur.prefix + cur.label
                # print(prefix)
                cur.sons[c] = TreeNode(c, prefix)
            cur = cur.sons.get(c)
        # 单词字母遍历结束，添加单词解释
        cur.explanation = explanation
        cur.is_word = True
        # print(cur.explanation)

    @property
    def root(self):
        return self._root


def dfs_by_stack(root):
    """
    使用栈来实现深度优先搜索 (栈 先进后出)
    :param root: TreeNode 类型的根节点
    :return:
    """
    stack = list()  # 每个元素都是 TreeNode 类型
    stack.append(root)  # 初始化时，压入根节点
    while len(stack) > 0:  # 只要栈里还有节点，继续下去
        node = stack.pop()  # 弹出栈顶节点
        if node.is_word:
            print(node.prefix + node.label, node.explanation)  # 是一个单词，则输出
            if len(node.sons) == 0:
                continue
        # 非叶子节点 遍历它的每个子节点
        # 注意 这里使用了一个临时的栈，是为了保证遍历的顺序和递归遍历的顺序是一致的
        # 如果不要求一致，可以直接压入 stack
        stack_temp = [node.sons.get(son) for son in node.sons]  # 非递归
        while len(stack_temp) > 0:
            stack.append(stack_temp.pop())


if __name__ == "__main__":
    testTree = Tree()
    word_dict = {'love': '爱', 'like': '喜欢', 'successful': '成功的', 'success': '成功'}
    for _word, _explanation in word_dict.items():  # 构建前缀树
        testTree.add(_word, _explanation)
    dfs_by_stack(testTree.root)  # 深度优先搜索
