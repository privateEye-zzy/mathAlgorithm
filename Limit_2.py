# 计算两个重要极限
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce
# 计算n阶阶乘
def factorial(n):
    return reduce(lambda x, y: x * y, [1] + list(range(1, n + 1)))
# 计算多项式：1/n!*(1-1/n)*(1-2/n)*...*(1-(n-1)/n)
def polynomial(n):
    ret = 1.0
    for i in range(1, n, 1):
        ret *= 1 - i / n
    ret = 1.0 / factorial(n) * ret
    return ret
# 计算第一个重要极限，使用图形展示结果
def f1():
    x = np.linspace(-30 * np.pi, 30 * np.pi, 2000, endpoint=True)
    y = np.sin(x) / x
    plt.plot(x, y, color='r', label='sin(x)/x')
    plt.legend()
    plt.show()
# 计算第二个重要极限：使用(1+1/n)^n的牛顿展开式
def f2(iter=10):
    ret = 0.0
    for n in range(iter):
        ret += polynomial(n=n)
    print(ret)
if __name__ == "__main__":
    # f1()
    f2(iter=50)
