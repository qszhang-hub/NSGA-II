# *************************
# Author : ZhangQingshuai
# Time : 2022/8/30 10:34
# *************************
import numpy as np


def cal_crowding_distance(pop, F):
    n_f = len(F)  # 获取等级数量
    for i in range(n_f):
        costs = [pop[j].cost for j in F[i]]  # 取出当前等级所有个体的目标函数值
        n = len(costs)  # 当前等级个体数量
        n_obj = len(costs[0])  # 目标函数个数
        d = np.zeros([n, n_obj])  # 存放当前等级内n个个体n_obj个目标函数值的拥挤度
        for j in range(n_obj):  # 遍历每个目标函数值
            costs_j = [cost[j] for cost in costs]  # 取出所有个体的当前目标函数值
            ordered_cost_j = sorted(costs_j)  # 对当前目标函数值进行升序排序
            sorted_id = sorted(range(len(costs_j)), key=lambda x: costs_j[x])  # 获取升序排序索引
            d[sorted_id[0], j] = np.inf  # 定义最小的目标函数值的拥挤度为无穷大
            d[sorted_id[-1], j] = np.inf  # 定义最大的目标函数值的拥挤度为无穷大
            length = abs(ordered_cost_j[-1] - ordered_cost_j[0])
            if length == 0:  # 最大值与最小值之差若为0，说明列表内所有值都一样
                for k in range(1, n - 1):
                    d[sorted_id[k], j] = 0
            else:
                for k in range(1, n - 1):  # 遍历除了最小和最大以外的其他目标函数值个体
                    # 前一个减去后一个的绝对值，除以最大值减最小值
                    d[sorted_id[k], j] = abs(ordered_cost_j[k + 1] - ordered_cost_j[k - 1]) / length
        for m in range(n):  # 设置当前等级个体的拥挤度为总拥挤度
            pop[F[i][m]].crowding_distance = sum(d[m, :])
    return pop
