# *************************
# Author : ZhangQingshuai
# Time : 2022/8/30 11:59
# *************************
import matplotlib.pyplot as plt
import scipy.io as sio


def plot_costs(cost1, cost2):
    # plt.plot(cost1, cost2, 'r*', 10)
    plt.scatter(cost1, cost2, facecolors='none', edgecolors='blue')
    # plt.scatter(cost1, cost2)
    plt.xlabel('f1')
    plt.ylabel('f2')
    plt.title('Pareto Front')
    plt.grid(True)


if __name__ == '__main__':
    # (题号，第几轮，hv值)  这个要看运行出来的结果，自己对照，找出最优结果所在轮数.
    for index, run, hv in [(1, 13, 0.593331015), (2, 11, 0.071466561), (3, 14, 0.285476977), (5, 6, 0.417684847),
                           (7, 18, 0.364204801)]:
        pop = sio.loadmat('Result/NSGA2_Pop_' + str(index) + '_' + str(run) + '.mat')['Pop']
        plt.clf()
        cost1 = [p[0] for p in pop]
        cost2 = [p[1] for p in pop]
        plot_costs(cost1, cost2)
        plt.title('HV=%f' % hv)
        # plt.show()
        plt.savefig('Figure/NSGA2_RWCMOP_%d_best_hv.png' % index, dpi=300)
