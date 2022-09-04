# *************************
# Author : ZhangQingshuai
# Time : 2022/8/30 11:51
# *************************
def sort_pop(pop):
    # 按照拥挤度对种群进行降序排序
    pop = sorted(pop, key=lambda x: x.crowding_distance, reverse=True)  # 降序排列
    # 按照非支配排序等级对种群进行升序排序
    pop = sorted(pop, key=lambda x: x.rank)  # 升序排列
    return pop
