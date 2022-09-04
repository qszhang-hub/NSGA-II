# *************************
# Author : ZhangQingshuai
# Time : 2022/8/29 21:29
# *************************
class Individual:
    def __init__(self):
        self.position = []  # 解
        self.cost = []  # 目标函数值
        self.rank = 0  # 非支配排序等级
        self.domination = []  # 支配集合
        self.dominated = 0  # 被支配次数
        self.crowding_distance = 0  # 拥挤度
        self.cv = 0  # 约束违反值(constraint violation value)
