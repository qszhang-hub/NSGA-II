# *************************
# Author : ZhangQingshuai
# Time : 2022/8/30 11:37
# *************************
import random

from create_x import create_x


def mutate(x, mu, var_min, var_max, step):
    n = len(x)
    for i in range(n):
        if random.random() < mu:
            x[i] = create_x(var_min, var_max, step)[i]
    return x


# Routine for real polynomial mutation of an individual
# 实数编码的常规多项式变异
def mutation_real(x, mu, var_min, var_max, eta_m):
    """
    :param x: 个体
    :param mu: 变异概率
    :param var_min: 各变量最小值
    :param var_max: 各变量最大值
    :param eta_m: 分布指数η_m
    :return: 变异后的个体
    """
    n = len(x)
    for i in range(n):
        r = random.random()
        # 对个体某变量进行变异
        if r < mu:  # 满足变异概率才进行变异
            v = x[i]
            low = var_min[i]
            up = var_max[i]
            delta1 = (v - low) / (up - low)
            delta2 = (up - v) / (up - low)
            # delta=min(delta1, delta2)
            r = random.random()
            mut_pow = 1.0 / (eta_m + 1.0)
            if r <= 0.5:
                xy = 1.0 - delta1
                val = 2.0 * r + (1.0 - 2.0 * r) * (xy ** (eta_m + 1.0))
                delta = val ** mut_pow - 1.0
            else:
                xy = 1.0 - delta2
                val = 2.0 * (1.0 - r) + 2.0 * (r - 0.5) * (xy ** (eta_m + 1.0))
                delta = 1.0 - val ** mut_pow
            v = v + delta * (up - low)
            # 控制范围不超过变量的范围
            v = min(up, max(v, low))
            x[i] = v
    return x

