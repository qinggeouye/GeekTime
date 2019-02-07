# coding=utf-8
import copy


def merge_sort(to_sort=None):
    """
    使用函数的递归（嵌套）调用，实现归并排序（从小到大）
    :param to_sort: 等待排序的数组
    :return: 排序后的数组
    """
    if to_sort is None:
        return []
    # 如果分解到只剩一个数，返回该数
    if len(to_sort) == 1:
        return to_sort
    # 将数组分解成左右两半
    mid = len(to_sort) / 2
    left = copy.copy(to_sort[0:mid])
    right = copy.copy(to_sort[mid:len(to_sort)])
    # 嵌套调用 对两半数组分别进行排序
    left = merge_sort(left)
    right = merge_sort(right)
    # 合并排序后的两半
    merged = merge(left, right)

    return merged


def merge(left=None, right=None):
    """
    合并两个已经排序完毕的数组（从小到大）
    :param left: 左半边数组
    :param right: 右半边数组
    :return: 合并后的数组
    """
    if left is None:
        left = []
    if right is None:
        right = []
    merged_one = list()
    ai = 0
    bi = 0
    # 轮流从两个数组中取出较小的值 放入合并后的数组中
    while ai < len(left) and bi < len(right):
        if left[ai] <= right[bi]:
            merged_one.append(left[ai])
            ai = ai + 1
        else:
            merged_one.append(right[bi])
            bi = bi + 1
    # 将某个数组内剩余的数字放入合并后的数组中
    if ai < len(left):
        for i in range(ai, len(left)):
            merged_one.append(left[i])
    else:
        for i in range(bi, len(right)):
            merged_one.append(right[i])
    return merged_one


if __name__ == '__main__':
    to_sort_ = [3434, 3356, 67, 12334, 878667, 387]
    sorted_ = merge_sort(to_sort_)
    print(sorted_)
