# *************************
# Author : ZhangQingshuai
# Time : 2022/8/30 11:32
# *************************
import random


def crossover(x1, x2):
    n = len(x1)
    i = random.randint(0, n - 1)
    y1, y2 = x1, x2
    y1[i] = x2[i]
    y2[i] = x1[i]
    return y1, y2


# # 实数编码,SBX交叉
# def crossover(pop, var_min, var_max, eta=1.0, pcross_real=1):
#     """
#
#     :param pop: 种群
#     :param var_min: 各变量最小值
#     :param var_max: 各变量最大值
#     :param eta: 分布因子η
#     :param pcross_real: 交叉概率
#     :return:
#     """
#     n = len(pop)  # 种群数量
#     m = len(pop[0])  # 个体变量个数
#     for i in range(0, n, 2):
#         # 如果随机概率大于交叉概率则不进行交叉操作
#         if random.random() > pcross_real:
#             continue
#
#         # 对两个个体执行SBX交叉操作
#         for j in range(m):
#             # 对某自变量交叉
#             ylow = var_min[j]  # 该变量最小值
#             yup = var_max[j]  # 该变量最大值
#             x1 = pop[i][j]
#             x2 = pop[i + 1][j]
#             r = random.random()
#             # 求β
#             if r <= 0.5:
#                 beta = (2 * r) ** (1.0 / (eta + 1.0))
#             else:
#                 beta = (1.0 / (2 - 2 * r)) ** (1.0 / (eta + 1.0))
#             # 求后代个体变量
#             c1 = 0.5 * ((1 + beta) * x1 + (1 - beta) * x2)
#             c2 = 0.5 * ((1 - beta) * x1 + (1 + beta) * x2)
#             # 控制范围，不能超出变量范围
#             c1 = min(max(c1, ylow), yup)
#             c2 = min(max(c2, ylow), yup)
#
#             pop[i][j] = c1
#             pop[i + 1][j] = c2
# 实数编码,SBX交叉
def crossover_real(x1, x2, var_min, var_max, eta_c=1.0):
    """
    :param x1: 个体1
    :param x2: 个体2
    :param var_min: 各变量最小值
    :param var_max: 各变量最大值
    :param eta_c: 分布因子η_c
    :return: 交叉后的个体x1和x2
    """
    n = len(x1)  # 个体变量个数
    # 对两个个体执行SBX交叉操作
    for i in range(n):
        # 对某自变量交叉
        low = var_min[i]  # 该变量最小值
        up = var_max[i]  # 该变量最大值
        x1_i = x1[i]
        x2_i = x2[i]
        r = random.random()
        # 求β
        if r <= 0.5:
            beta = (2 * r) ** (1.0 / (eta_c + 1.0))
        else:
            beta = (1.0 / (2 - 2 * r)) ** (1.0 / (eta_c + 1.0))
        # 求后代个体变量
        c1 = 0.5 * ((1 + beta) * x1_i + (1 - beta) * x2_i)
        c2 = 0.5 * ((1 - beta) * x1_i + (1 + beta) * x2_i)
        # 控制范围，不能超出变量范围
        x1[i] = min(max(c1, low), up)
        x2[i] = min(max(c2, low), up)
    return x1, x2
