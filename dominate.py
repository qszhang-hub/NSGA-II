# *************************
# Author : ZhangQingshuai
# Time : 2022/8/29 22:10
# *************************
# pareto支配关系，当p的所有值都小于等于q中对应值，且至少有一个值小于q中对应值时，说明p支配q。
def pareto_dominate(p, q):  # 判断个体p是否pareto支配个体q
    n = len(p.cost)
    ans = 0
    for i in range(n):
        if p.cost[i] > q.cost[i]:
            return False
        if p.cost[i] < q.cost[i]:
            ans += 1
    if ans > 0:  # 说明p中至少有一个值小于q中的对应值，且整体上所有值都小于等于q中对应值
        return True
    else:
        return False


def constrained_dominate(p, q):  # 判断个体p是否约束支配个体q
    if p.cv == 0 and q.cv == 0:  # 都是可行解，看是否pareto支配
        if pareto_dominate(p, q):
            return True
        else:
            return False
    elif p.cv == 0 and q.cv > 0:  # 一个可行解，一个不可行解，可行解约束支配不可行解
        return True
    elif p.cv > 0 and q.cv > 0:  # 都不可行，cv值小的约束支配cv值大的
        if p.cv < q.cv:
            return True
        else:
            return False
    else:
        return False
