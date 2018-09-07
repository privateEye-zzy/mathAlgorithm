'''
高度为h的斜抛运动模型，求：最远距离x，运动时间t和出手角度r
'''
import numpy as np
import matplotlib.pyplot as plt
from math import tan, sqrt, atan2, atan
plt.rcParams['font.sans-serif'] = ['SimHei']
# 二次函数求极值
def quadratic_fun_extreme(A, B, C):
    x_center = - B / (2 * A)
    y_center = (4 * A * C - B**2) / (4 * A)
    return x_center, y_center
# 二次函数求根公式
def quadratic_fun_root(A, B, C):
    deta = B**2 - 4*A*C
    return (-B + sqrt(deta)) / (2 * A), (-B - sqrt(deta)) / (2 * A)
# 解法一：构造关于时间t的二次函数求极值的方法
def solve1():
    A = -1 / 4 * g**2
    B = v0**2 + g*h
    C = -h**2
    t2, x2 = quadratic_fun_extreme(A, B, C)
    r = atan2(v0, sqrt(v0**2 + 2*g*h))  # 极值角度条件
    t, x, r = sqrt(t2), sqrt(x2), r * 180 / np.pi
    return t, x, r
# 解法二：构造关于水平位移x的二次函数求根的插值计算法
def solve2():
    hx = []
    rs = np.arange(1, 90, 0.1)  # 角度取值范围
    for r in rs:
        l = r * np.pi / 180
        A = -g / (2 * v0**2) * (1 + tan(l)**2)  # 系数带有非线性函数tanx，采用插值算法
        B = tan(l)
        C = h
        hx.append(max(quadratic_fun_root(A=A, B=B, C=C)))
    max_idx = np.argmax(hx)
    x, r = hx[max_idx], rs[max_idx]
    t = x / (v0 * np.cos(r * np.pi / 180))
    return t, x, r
# 解法三：分析矢量速度三角形面积相等，化双变量为单变量
def solve3():
    v = sqrt(v0**2 + 2 * g * h)
    x = (v0 * v) / g
    r = atan2(v0, v)
    t = x / (v0 * np.cos(r))
    return t, x, r * 180 / np.pi
# 解法四：包络线方程
def solve4():
    x = v0 / g * sqrt(v0**2 + 2*g*h)
    r = atan(v0**2 / (g * x))
    t = x / (v0 * np.cos(r))
    return t, x, r * 180 / np.pi
# 画图：安全抛物线
def draw_track(x_max):
    fig = plt.figure()
    plt.xlim(0, x_max + 1)
    ax = fig.add_subplot(111)
    safe_xs = np.arange(0, x_max, 0.1)
    safe_ys = []
    for i in safe_xs:
        gxi = -g / (2 * v0 ** 2) * i ** 2 + v0 ** 2 / (2 * g)  # 包络线方程
        safe_ys.append(gxi + h)
    plt.ylim(0, max(safe_ys) + 0.5)
    rs = [0] + (90 * np.random.random_sample(50) + 1).tolist()  # 随机任何斜抛的角度
    for r in rs:
        l = r * np.pi / 180
        A = -g / (2 * v0 ** 2) * (1 + tan(l) ** 2)
        B = tan(l)
        C = h
        x = max(quadratic_fun_root(A=A, B=B, C=C))
        t = x / (v0 * np.cos(l))
        ts = np.arange(0, 2 * t, 0.1)
        xs = v0 * np.cos(l) * ts
        ys = v0 * np.sin(l) * ts - 1 / 2 * g * ts**2 + h
        ax.plot(xs, ys, color='green' if r == 0 else 'red', linestyle='-')
    ax.plot(safe_xs, safe_ys, color='#424242', linestyle='-', label='包络线方程')
    plt.legend()
    plt.show()
if __name__ == '__main__':
    v0, h, g = 10.0, 1.7, 9.78
    t1, x1, r1 = solve1()
    print('解法一：数学方法：构造关于时间t的二次函数的求极值方法，最优时间：{}秒，最远距离：{}米，极值角度：{}度'.format(
        round(t1, 2), round(x1, 2), round(r1, 2)))
    t2, x2, r2 = solve2()
    print('解法二：编程方法：构造关于水平位移x的二次函数求根的插值计算法，最优时间：{}秒，最远距离：{}米，极值角度：{}度'.format(
        round(t2, 2), round(x2, 2), round(r2, 2)))
    t3, x3, r3 = solve3()
    print('解法三：数学方法：分析矢量速度三角形面积相等，化双变量为单变量，最优时间：{}秒，最远距离：{}米，极值角度：{}度'.format(
        round(t3, 2), round(x3, 2), round(r3, 2)))
    t4, x4, r4 = solve4()
    print('解法四：数学方法：包络线方程，最优时间：{}秒，最远距离：{}米，极值角度：{}度'.format(
        round(t4, 2), round(x4, 2), round(r4, 2)))
    # draw_track(x_max=x4)
