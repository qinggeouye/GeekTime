import time


def odd_even_num():
    even_cnt = 0
    odd_cnt = 0
    # 使用位运算，判断奇数和偶数
    start = time.time()
    for i in range(10000000):
        if i & 1 == 0:
            even_cnt = even_cnt + 1
        else:
            odd_cnt = odd_cnt + 1
    end = time.time()
    print(end - start)
    even_cnt, odd_cnt = 0, 0
    # 使用模运算，判断奇数和偶数
    start = time.time()
    for i in range(10000000):
        if i % 2 == 0:
            even_cnt = even_cnt + 1
        else:
            odd_cnt = odd_cnt + 1
    end = time.time()
    print(end - start)


def switch_two_num(x, y):
    """
    异或的两个特性：两个相等的数的异或等于0，任何一个数和0异或之后还是这个数不变
    :param x:
    :param y:
    :return:
    """
    print("x=%s, y=%s" % (x, y))
    x = x ^ y
    y = x ^ y
    x = x ^ y
    print(f"x={x}, y={y}")


def set_operate(a, b):
    # 两个集合 a 和 b，如 a=[1, 3, 8] b=[4, 8]
    # 分别转为 8 位的二进制数
    bit_a = 0
    bit_b = 0
    # 初级实现
    for i in range(len(a)):
        bit_a = bit_a + 2**(a[i]-1)
    for i in range(len(b)):
        bit_b = bit_b + 2**(b[i]-1)
    s = bit_a & bit_b
    print("bit_a=%s, bit_b=%s, s=%s" % (bit_a, bit_b, s))


if __name__ == '__main__':
    odd_even_num()
    switch_two_num(5, 9)
    set_operate([1, 3, 8], [4, 8])
