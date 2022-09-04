# *************************
# Author : ZhangQingshuai
# Time : 2022/8/29 20:50
# *************************
import numpy as np
import scipy.io as sio
from matplotlib import pyplot as plt

from Individual import Individual
from RWCMOPs import RWCMOP
from cal_crowding_distance import cal_crowding_distance
from create_x import create_x
from crossover import crossover, crossover_real
from fast_non_dominated_sort import fast_non_dominated_sort
from mutate import mutate, mutation_real
from plot_costs import plot_costs
from sort_pop import sort_pop
from tournament_select import tournament_select


def main(n_var, n_obj, n_pop, max_iter, pc, mu, var_min, var_max, step, cost_and_cv_function, eta_c=20, eta_m=20):
    nc = round(pc * n_pop / 2) * 2  # 根据交叉比例得到子代种群规模大小
    pop = [Individual() for _ in range(n_pop)]  # 生成n_pop个个体作为种群
    # plt.figure(dpi=160)
    # plt.ion()  # 设置为交互模式
    # 初始化种群
    for i in range(n_pop):
        pop[i].position = create_x(var_min, var_max, step)
        pop[i].cost, pop[i].cv = cost_and_cv_function(pop[i].position)
    # 快速非支配排序
    pop, F = fast_non_dominated_sort(pop)
    # 拥挤度计算
    pop = cal_crowding_distance(pop, F)
    # 遗传算法主程序
    for i in range(max_iter):
        pop_c = [[Individual() for _ in range(2)] for _ in range(nc // 2)]  # 生成nc/2行，2列的种群
        for j in range(nc // 2):  # 交叉
            p1 = tournament_select(pop)
            p2 = tournament_select(pop)
            pop_c[j][0].position, pop_c[j][1].position = crossover_real(p1.position, p2.position, var_min, var_max, eta_c)
        pop_c = [p for couple in pop_c for p in couple]  # 展开列表
        for k in range(nc):  # 变异
            pop_c[k].position = mutation_real(pop_c[k].position, mu, var_min, var_max, eta_m)
            pop_c[k].cost, pop_c[k].cv = cost_and_cv_function(pop_c[k].position)
        new_pop = pop + pop_c  # 新一代种群=父代种群+子代种群
        # 对合并后的种群进行快速非支配排序
        pop, F = fast_non_dominated_sort(new_pop)
        # 对合并后的种群进行拥挤度计算
        pop = cal_crowding_distance(pop, F)
        # 对合并后的种群进行排序
        pop = sort_pop(pop)
        # 淘汰，仅选取前n_pop个个体作为种群
        pop = pop[: n_pop]
        pop, F = fast_non_dominated_sort(pop)
        pop = cal_crowding_distance(pop, F)
        pop = sort_pop(pop)
        F0 = [pop[j] for j in F[0]]
        print('Iteration: %d   Number of F0 Members = %d' % (i + 1, len(F0)))
    #     plt.clf()  # 清除上一帧图像
    #     cost1 = [p.cost[0] for p in pop]
    #     cost2 = [p.cost[1] for p in pop]
    #     plot_costs(cost1, cost2)
    #     plt.pause(0.01)  # 每一帧暂停0.01s
    # plt.ioff()  # 关闭交互模式
    # plt.show()  # 显示结果
    cost = [p.cost for p in F0]
    cost = np.array(cost)
    return cost


if __name__ == '__main__':
    n_pop = 121  # 种群大小
    max_iter = 100  # 最大迭代次数
    pc = 0.9  # 交叉比例
    eta_c = 20  # 模拟二进制交叉分布指数
    eta_m = 20  # 多项式变异分布指数
    n_runs = 20  # 运行轮数
    for index in [1, 2, 3, 5, 7]:  # 选择题目
        for run in range(n_runs):  # 运行n_runs轮
            n_var, n_obj, var_min, var_max, step, cost_and_cv_function = RWCMOP(index)
            # if n_obj == 2:
            #     n_pop = 80
            # if n_var <= 10:
            #     max_iter = 2500
            mu = 1 / n_var  # 变异概率
            # mu = 0.2  # 变异概率
            cost = main(n_var, n_obj, n_pop, max_iter, pc, mu, var_min, var_max, step, cost_and_cv_function)
            print(cost)
            sio.savemat('Result/NSGA2_Pop_' + str(index) + '_' + str(run + 1) + '.mat', {'Pop': cost})  # 保存结果
