# *************************
# Author : ZhangQingshuai
# Time : 2022/8/29 21:25
# *************************
import random


def create_x(var_min, var_max, step):  # 实数编码
    n = len(var_min)  # 获取基因长度
    x = []
    for i in range(n):
        if step[i] != 0:  # 如果给出了步长，则按照步长生成随机变量
            x.append(var_min[i] + random.randint(0, (var_max[i] - var_min[i]) // step[i]) * step[i])
        else:  # 若未给出步长，则生成区间内随机的浮点数
            x.append(random.uniform(var_min[i], var_max[i]))
    return x
