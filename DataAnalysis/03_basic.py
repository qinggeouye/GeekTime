# 如果我想在 Python 中引用 scikit-learn 库该如何引用？
import sklearn


# 求 1+3+5+7+…+99 的求和，用 Python 该如何写？
# 递归
def sum_recruit(n):
    if n <= 0:
        return 0
    return n + sum_recruit(n - 2)


m = 99
print(sum(range(m, 0, -2)))
print(sum_recruit(m))
