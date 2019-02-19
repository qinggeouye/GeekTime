# https://blog.csdn.net/Annihilation7/article/details/85209360


class TrieNode(object):
    def __init__(self, is_word=False):
        self.is_word = is_word  # 是否是一个单词，默认为 False
        self.next = dict()  # key 是单个字符，value 是下一个节点


class Trie:
    def __init__(self):
        self._root = TrieNode()
        self._size = 0  # 初始化为 0

    def is_empty(self):
        return self._size == 0  # 判空

    def get_size(self):
        return self._size  # 获取树的 size

    def contains(self, word):
        """
        判断单词 word 是否存在于树中 非递归方法
        :param word: 待查找单词
        :return:
        """
        cur = self._root  # 从根节点开始
        for character in word:
            cur = cur.next.get(character, None)  # 查找下一个节点中的字典，没找到返回 None
            if cur is None:
                return False
        return cur.is_word is True

    def contains_recruit(self, node, word, index):
        """
        判断单词 word 是否存在于树中 递归方法
        :param node: 当前节点
        :param word: 待查找单词
        :param index: 此时到达 word 的哪个 element，即 word[index] 是待考察的 element
        :return:
        """
        if index == len(word):  # 递归到底的情况，注意最后一个元素的 is_word 是不是 True
            if node.is_word:
                return True
            return False

        dst_element = word[index]
        # 如果当前节点的 next 的 dict 键中不包含 dst_element
        if node.next.get(dst_element, None) is None:
            return False
        # 否则去到 node 的 next 中以 dst_element 为键的 Node 是否包含 word[index + 1]
        return self.contains_recruit(node.next[dst_element], word, index+1)

    def add(self, word):
        """
        向 Trie 中添加一个 单词 word，注意不是单个字符  迭代方法
        :param word: 待添加的单词
        :return:
        """
        if self.contains(word):  # 先判断是否已经存在
            return
        # 从根节点开始，Trie 的字符串全部是从根节点开始的
        cur = self._root
        for character in word:
            # 如果 next node 中以 character 为键的值不存在
            if cur.next.get(character, None) is None:
                # 则新建一个 Node 作为 character 的值
                cur.next[character] = TrieNode()
            # 更新 cur 到下一个以 character 为边的 Node
            cur = cur.next.get(character)
        # 添加单词，单词尾部的 element 的is_word 一定为 True
        cur.is_word = True
        self._size += 1

    def add_recruit(self, node, word, index):
        """
        向 Trie 树中添加一个单词  递归方法
        :param node: 当前节点
        :param word: 待添加的单词
        :param index: 此时到达 word 的哪个 element，即 word[element] 是待考察的 element
        :return:
        """
        # 递归到底的情况，可能涉及更新当前节点的 is_word
        if index == len(word):
            if not node.is_word:
                node.is_word = True
                self._size += 1
            return

        dst_element = word[index]
        # 如果当前节点的 next 的 dict 键中不包含 dst_element
        if node.next.get(dst_element, None) is None:
            # 就为这个键新建一个 Node
            node.next[dst_element] = TrieNode()
        return self.add_recruit(node.next[dst_element], word, index+1)

    def is_prefix(self, prefix):
        """
        查询是否在 Trie 中有单词以 prefix 为前缀，注意 'abc' 也是 'abc' 的前缀  非递归方法
        :param prefix: 待查询字符串
        :return:
        """
        cur = self._root
        for character in prefix:
            cur = cur.next.get(character, None)
            if cur is None:
                return False
        return True


if __name__ == "__main__":
    test = Trie()  # 测试非递归版本
    test_recruit = Trie()  # 测试递归版本

    record = ['你好', 'hello', 'こんにちは', 'pan', 'panda', '我是大哥大666']

    print('初始化是否为空：', test.is_empty())
    print('此时的 size ：', test.get_size())
    print('将 record 中的字符串全部添加进 test：')
    for elem in record:
        test.add(elem)
    print('判断 record 中元素是否都已经存在于 test 中：')
    for elem in record[::-1]:
        flag = test.contains(elem)
        if flag:
            print('"%s" 存在于 test 中' % elem)
    print("此时的 test 的 size：", test.get_size())
    print('"hel" 是否是 test 的前缀：', test.is_prefix('hel'))
