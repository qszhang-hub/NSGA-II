# *************************
# Author : ZhangQingshuai
# Time : 2022/8/29 22:06
# *************************
from dominate import pareto_dominate, constrained_dominate


def fast_non_dominated_sort(pop):
    n_pop = len(pop)
    F = [[]]  # 存放所有等级个体的下标
    for i in range(n_pop):  # 清空种群所有个体的支配集和被支配次数
        pop[i].domination = []
        pop[i].dominated = 0
    # 找出所有等级为0的个体(即未被其他任何个体支配的个体)
    for i in range(n_pop):
        for j in range(i + 1, n_pop):
            if constrained_dominate(pop[i], pop[j]):
                pop[i].domination.append(j)
                pop[j].dominated += 1
            elif constrained_dominate(pop[j], pop[i]):
                pop[j].domination.append(i)
                pop[i].dominated += 1
        if pop[i].dominated == 0:
            pop[i].rank = 0
            F[0].append(i)
    # 找出其他等级的个体
    k = 0  # 初始化为等级0
    while True:
        Q = []  # 存放下一等级个体的所有下标
        for i in F[k]:  # 遍历等级为k的所有个体
            for j in pop[i].domination:  # 遍历每个等级为k的个体的支配集，将其被支配次数减一
                pop[j].dominated -= 1
                if pop[j].dominated == 0:  # 若被支配次数减一后，其被支配次数为0
                    Q.append(j)  # 说明j就属于下一等级
                    pop[j].rank = k + 1  # 设置j的等级为k+1
        if len(Q) == 0:  # 当没有下一等级的个体时，说明已经完成了所有等级的录入，退出循环
            break
        else:  # 否则，将得到的下一等级个体集合放入总集合F中，k+1，继续循环
            F.append(Q)
            k += 1
    return pop, F
