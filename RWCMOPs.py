# *************************
# Author : ZhangQingshuai
# Time : 2022/8/30 19:05
# *************************
from numpy import pi, sqrt


def RWCMOP(i):  # i为题号，从1开始
    if i == 1:
        n_var = 4  # 变量个数
        n_obj = 2  # 待优化目标函数数量
        var_min = [0.51, 0.51, 10, 10]  # 各变量最小值
        var_max = [99.49, 99.49, 200, 200]  # 各变量最大值
        step = [0, 0, 0, 0]  # 各变量步长 0代表未给出步长

        def cost_and_cv_function(x):  # 目标函数以及约束条件
            x1, x2, x3, x4 = x
            x1, x2 = round(x1), round(x2)
            z1 = 0.0625 * x1
            z2 = 0.0625 * x2
            f1 = 1.7781 * z1 * (x3 ** 2) + 0.6224 * z1 * x2 * x4 + 3.1661 * (z1 ** 2) * x4 + 19.84 * (z1 ** 2) * x3
            f2 = - pi * (x3 ** 2) * x4 - (4 / 3) * pi * (x3 ** 3)
            g1 = 0.00954 * x3 - z2
            g2 = 0.0193 * x3 - z1
            # if 0.00954 * x[2] > z2 or 0.0193 * x[2] > z1:
            #     f1 = f2 = inf
            cv = max(g1, 0) + max(g2, 0)  # cv值
            return [f1, f2], cv

    elif i == 2:
        n_var = 5  # 变量个数
        n_obj = 2  # 待优化目标函数数量
        var_min = [0.05, 0.2, 0.2, 0.35, 3]  # 各变量最小值
        var_max = [0.5, 0.5, 0.6, 0.5, 6]  # 各变量最大值
        step = [0, 0, 0, 0, 0]  # 各变量步长 0代表未给出步长

        def cost_and_cv_function(x):  # 目标函数以及约束条件
            rho1, rho2, rho3 = 100, 2770, 7780
            E1, E2, E3 = 1.6, 70, 200
            c1, c2, c3 = 500, 1500, 800
            d1, d2, d3, b, L = x
            EI = (2 * b / 3) * (E1 * (d1 ** 3) + E2 * (d2 ** 3 - d1 ** 3) + rho3 * (d3 - d2))
            mu = 2 * b * (rho1 * d1 + rho2 * (d2 - d1) + rho3 * (d3 - d2))
            f1 = (-pi / (2 * L) ** 2) * sqrt(abs(EI / mu))
            f2 = 2 * b * L * (c1 * d1 + c2 * (d2 - d1) + c3 * (d3 - d2))
            g1 = mu * L - 2800
            g2 = d1 - d2
            g3 = d2 - d1 - 0.15
            g4 = d2 - d3
            g5 = d3 - d2 - 0.01
            # if miu * x[4] - 2800 > 0 or x[0] - x[1] > 0 or x[1] - x[0] - 0.15 > 0 or x[1] - x[2] > 0 or \
            #         x[2] - x[1] - 0.01 > 0:
            #     f1 = f2 = inf
            cv = max(g1, 0) + max(g2, 0) + max(g3, 0) + max(g4, 0) + max(g5, 0)
            return [f1, f2], cv

    elif i == 3:
        n_var = 3  # 变量个数
        n_obj = 2  # 待优化目标函数数量
        var_min = [1e-5, 1e-5, 1]  # 各变量最小值
        var_max = [100, 100, 3]  # 各变量最大值
        step = [0, 0, 0]  # 各变量步长 0代表未给出步长

        def cost_and_cv_function(x):  # 目标函数以及约束条件
            x1, x2, x3 = x
            f1 = x1 * sqrt(16 + x3 ** 2) + x2 * sqrt(1 + x3 ** 2)
            f2 = (20 * sqrt(16 + x3 ** 2)) / (x3 * x1)
            g1 = f1 - 0.1
            g2 = f2 - 1e5
            g3 = (80 * sqrt(1 + x3 ** 2)) / (x3 * x2) - 1e5
            # if f1 - 0.1 > 0 or f2 - 1e5 > 0 or (80 * sqrt(1 + x[2] ** 2)) / (x[2] * x[1]) - 1e5 > 0:
            #     f1 = f2 = inf
            cv = max(g1, 0) + max(g2, 0) + max(g3, 0)
            return [f1, f2], cv
    # elif i == 4:
    #     n_var = 4  # 变量个数
    #     n_obj = 2  # 待优化目标函数数量
    #     var_min = [0.125, 0.1, 0.1, 0.125]  # 各变量最小值
    #     var_max = [5, 10, 10, 5]  # 各变量最大值
    #     step = [0, 0, 0, 0]  # 各变量步长 0代表未给出步长
    #
    #     def cost_function(x):  # 目标函数以及约束条件
    #         P, L=6000,14
    #         E = 30*1e6
    #         t_max, sigma_max = 13600, 30000
    #         M = P*(L+x[1]/2)
    #         R = sqrt(((x[1]**2)/4)+((x[0]+x[2])/2)**2)
    #         J = 2*(sqrt(2)*x[0]*x[1]*(x[1]**2/12+((x[0]+x[2])/2)**2))
    #         sigma = 6*P*L/(x[3]*(x[2]**2))
    #         Pc = 4.013*E*sqrt(((x[2]**2)+(x[3]**6))/36)
    #         f1 = 4.9 * 1e-5 * (x[1] ** 2 - x[0] ** 2) * (x[3] - 1)
    #         f2 = 9.82 * 1e6 * ((x[1] ** 2 - x[0] ** 2) / (x[2] * x[3] * (x[1] ** 3 - x[0] ** 3)))
    #         if 20 - (x[1] - x[0]) > 0 or (x[2] / (3.14 * (x[1] ** 2 - x[0] ** 2))) - 0.4 > 0 or \
    #                 (2.22 * 1e-3 * x[2] * (x[1] ** 3 - x[0] ** 3)) / ((x[1] ** 2 - x[0] ** 2) ** 2) - 1 > 0 or \
    #                 900 - 2.66 * 1e-2 * (x[2] * x[3] * (x[1] ** 3 - x[0] ** 3) / (x[1] ** 2 - x[0] ** 2)) > 0:
    #             f1 = f2 = inf
    #         return f1, f2

    elif i == 5:
        n_var = 4  # 变量个数
        n_obj = 2  # 待优化目标函数数量
        var_min = [55, 75, 1000, 11]  # 各变量最小值
        var_max = [80, 110, 3000, 20]  # 各变量最大值
        step = [0, 0, 0, 0]  # 各变量步长 0代表未给出步长

        def cost_and_cv_function(x):  # 目标函数以及约束条件
            x1, x2, x3, x4 = x
            f1 = 4.9 * 1e-5 * (x2 ** 2 - x1 ** 2) * (x4 - 1)
            f2 = 9.82 * 1e6 * ((x2 ** 2 - x1 ** 2) / (x3 * x4 * (x2 ** 3 - x1 ** 3)))
            g1 = 20 - (x2 - x1)
            g2 = (x3 / (3.14 * (x2 ** 2 - x1 ** 2))) - 0.4
            g3 = (2.22 * 1e-3 * x3 * (x2 ** 3 - x1 ** 3)) / ((x2 ** 2 - x1 ** 2) ** 2) - 1
            g4 = 900 - 2.66 * 1e-2 * (x3 * x4 * (x2 ** 3 - x1 ** 3) / (x2 ** 2 - x1 ** 2))
            # if 20 - (x[1] - x[0]) > 0 or (x[2] / (3.14 * (x[1] ** 2 - x[0] ** 2))) - 0.4 > 0 or \
            #         (2.22 * 1e-3 * x[2] * (x[1] ** 3 - x[0] ** 3)) / ((x[1] ** 2 - x[0] ** 2) ** 2) - 1 > 0 or \
            #         900 - 2.66 * 1e-2 * (x[2] * x[3] * (x[1] ** 3 - x[0] ** 3) / (x[1] ** 2 - x[0] ** 2)) > 0:
            #     f1 = f2 = inf
            cv = max(g1, 0) + max(g2, 0) + max(g3, 0) + max(g4, 0)
            return [f1, f2], cv

    elif i == 7:
        n_var = 4  # 变量个数
        n_obj = 2  # 待优化目标函数数量
        var_min = [11.51, 11.51, 11.51, 11.51]  # 各变量最小值
        var_max = [60.49, 60.49, 60.49, 60.49]  # 各变量最大值
        step = [0, 0, 0, 0]  # 各变量步长 0代表未给出步长

        def cost_and_cv_function(x):  # 目标函数以及约束条件
            x1, x2, x3, x4 = x
            f1 = abs(6.931 - ((x3 * x4) / (x1 * x2)))
            f2 = max(x)
            g1 = f1 / 6.931 - 0.5
            # if f1 / 6.931 - 0.5 > 0:
            #     f1 = f2 = inf
            cv = max(g1, 0)
            return [f1, f2], cv

    return n_var, n_obj, var_min, var_max, step, cost_and_cv_function
