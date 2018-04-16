# 幂级数展开求解导数值的算法
import numpy as np
def fx(x):
    return np.sin(x) + x ** 0.5
def dfx(x):
    return np.cos(x) + 0.5 * x**-0.5
def series_expansion(x, h=1):
    ret = 1 / (2 * h) * (fx(x + h) - fx(x - h))  # 幂级数展开式
    loss = - 1 / 6 * h**2 * (-np.cos(x) + 3 / 8 * x**(-2.5))  # 幂级数理论误差项
    return round(ret, 8), round(loss, 8)
if __name__ == '__main__':
    x0 = 2
    hs = [1, 0.5, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001]  # 步长列表
    for h in hs:
        r, l = series_expansion(x=x0, h=h)
        print('当x={}，步长为{}时，fx的导数为{}，误差为{}'.format(x0, h, r, l))
    print('由fx的导函数直接求出为：{}'.format(round(dfx(x0), 8)))

