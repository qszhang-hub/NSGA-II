# *************************
# Author : ZhangQingshuai
# Time : 2022/8/30 11:15
# *************************
from random import sample


def tournament_select(pop):  # 锦标赛选择 选取原则：优先选取等级高的，同等级下选取拥挤度更大的
    p1, p2 = sample(pop, 2)  # 每次从种群中随机选取两个个体
    if p1.rank < p2.rank:
        p = p1
    elif p1.rank == p2.rank:
        if p1.crowding_distance > p2.crowding_distance:
            p = p1
        else:
            p = p2
    else:
        p = p2
    return p
