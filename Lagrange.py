# 求解y=sinx，其中x=0.3367
import math
# 线性插值算法
def L1(x, x0, y0, x1, y1):
    l1 = y0 * (x - x1) / (x0 - x1) + y1 * (x - x0) / (x1 - x0)
    M2 = round(math.fabs(-math.sin(max(x0, x1))), 4)
    R1 = 1 / 2 * M2 * math.fabs((x - x0) * (x - x1))
    return l1, R1
# 抛物线插值算法
def L2(x, x0, y0, x1, y1, x2, y2):
    l2 = y0 * ((x - x1) * (x - x2)) / ((x0 - x1) * (x0 - x2)) + y1 * ((x - x0) * (x - x2)) / ((x1 - x0) * (x1 - x2)) +\
         y2 * ((x - x0) * (x - x1)) / ((x2 - x0) * (x2 - x1))
    M3 = round(math.fabs(-math.cos(max(x0, x1))), 4)
    R2 = 1 / 6 * M3 * math.fabs((x - x0) * (x - x1) * (x - x2))
    return l2, R2
if __name__ == '__main__':
    x0, y0 = 0.32, 0.314567
    x1, y1 = 0.34, 0.333487
    x2, y2 = 0.36, 0.352274
    x = 0.3367
    l1, r1 = L1(x, x0, y0, x1, y1)
    print('sin(x={})的线性插值L1结果为：{}，其逼近误差为{}'.format(x, l1, r1))
    l2, r2 = L2(x, x0, y0, x1, y1, x2, y2)
    print('sin(x={})的抛物线插值L2结果为：{}，其逼近误差为{}'.format(x, l2, r2))
    print('sin(x={})api的计算结果为：{}'.format(x, math.sin(x)))
