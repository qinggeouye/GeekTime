# coding=utf-8
import copy

rewards = [1, 2, 5, 10]  # 四种面额的纸币


def get_all_components(total_rewards, result=None):
    """
    使用函数的递归（嵌套调用），找出所有可能的奖赏组合
    :param
        total_rewards 奖赏总金额
        result 保存当前的解
    :return: None
    """
    # 当 total_rewards=0 时，证明它是满足条件的解，结束嵌套调用，输出解
    if result is None:
        result = []
    if total_rewards == 0:
        print(result)
        return
    # 当 total_rewards<0 时，证明它不是满足条件的解，不输出
    elif total_rewards < 0:
        return
    else:
        for i in range(len(rewards)):
            new_result = copy.copy(result)  # 由于有4种情况，需要 clone 当前的解并传入被调用的函数
            new_result.append(rewards[i])  # 记录但当前但选择，解决一点问题
            get_all_components(total_rewards-rewards[i], new_result)  # 剩下但问题，留给嵌套调用去解决


if __name__ == '__main__':
    total_reward = 10
    get_all_components(total_reward)
