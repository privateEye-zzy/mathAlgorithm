'''
求解一阶非齐次线性微分方程
du / dt = u - 2t / u
u(0) = 1
求解u(t)
'''
import numpy as np
import matplotlib.pyplot as plt
# 伯努利方程算法
def bernoulli(ts):
    return np.power(1 + 2 * ts, 1/2)
# 微分方程右侧的函数
def ft(t, u):
    return u - (2 * t) / u
# Euler折线算法
def euler(ts, us, h=0.1):
    for i, t in enumerate(ts):
        us[i] = us[i - 1] + h * ft(ts[i - 1], us[i - 1]) if i != 0 else 1
    return us
if __name__ == '__main__':
    h = 0.05  # 步长，可尝试[0.05,0.01,0.001]
    start, end = 0, 2  # 区间
    l = (start + end) / h + 1  # 区间长度
    ts = np.linspace(start, end, int(l))  # 节点列表
    us = [0] * ts.shape[0]  # 节点对应的函数值列表
    ret_euler = euler(ts=ts, us=us, h=h)  # Ruler算法
    ret_bernoulli = bernoulli(ts=ts)  # Bernoulli算法
    # 绘制2x1个图形
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
    # 绘制第一个图，Ruler算法和Bernoulli算法的计算结果
    ax1.plot(ts, ret_euler, 'b', label='Euler')
    ax1.plot(ts, ret_bernoulli, 'r', label='Bernoulli')
    ax1.set_xlabel('t', fontsize=16)
    ax1.set_ylabel('u', fontsize=16)
    ax1.set_xlim(0, 2)
    ax1.set_ylim(0, 3)
    ax1.legend(loc=0)
    ax1.grid(True)
    # 绘制第二个图，Ruler算法和Bernoulli算法的误差
    ax2.plot(ts, ret_bernoulli - np.array(ret_euler), 'g', label='Error')
    ax2.set_xlabel('t', fontsize=16)
    ax2.set_ylabel('u(t) - u', fontsize=16)
    ax2.legend(loc=0)
    ax2.grid(True)
    plt.show()
