import copy

my_pwd = 'bada'  # 实际密码
pwd_char = ['a', 'b', 'c', 'd', 'e']  # 字符数组


def decrypt(char, password=None):
    """
    使用函数的递归（嵌套）调用，找出所有可能的 4 位密码
    :param char: 组成密码的字符
    :param password: 当前找出的密码
    :return:
    """
    if password is None:
        password = []
    if len(password) == 4:
        if "".join(password) == my_pwd:
            print(password)
            print("密码破解成功！")
            return True
        else:
            return False

    for i in range(len(char)):
        new_password = copy.copy(password)
        new_password.append(char[i])
        rest_char = copy.copy(char)
        if decrypt(rest_char, new_password):
            return True

    return False


if __name__ == "__main__":
    decrypt(pwd_char)
