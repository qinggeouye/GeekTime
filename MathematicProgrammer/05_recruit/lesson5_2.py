# coding=utf-8
import copy


def get_all_prod_factors(n, result=None):
    """
    使用递归编程，为给定的整数 n 找到所有可能的分解
    :param n: 整数
    :param result: 保存当前的分解
    :return: None
    """
    if result is None:
        result = []
    if n == 1:
        print('x'.join([str(_) for _ in result]))
        if 1 not in result:
            result.append(1)
            print('x'.join([str(_) for _ in result]))
    elif n < 0:
        return
    else:
        for i in range(1, n + 1):
            if (i == 1 and i not in result) or (i != 1 and n % i == 0):
                new_result = copy.copy(result)
                new_result.append(i)
                get_all_prod_factors(n // i, new_result)  # python3 // 表示整除，不带小数


if __name__ == '__main__':
    num = 8
    get_all_prod_factors(num)
