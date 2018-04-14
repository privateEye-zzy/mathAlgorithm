import numpy as np
import scipy.integrate as sci
def fx(x):
    return np.sin(x) / x
# 蒙特卡洛算法
def monteCarlo(start, stop, iter=20):
    ret = []
    for i in range(1, iter):
        np.random.seed(1000)
        x = np.random.random(i * 10) * (stop - start) + start
        ret.append(np.sum(fx(x)) / len(x) * (stop - start))
    return np.mean(ret)
# 复化矩形
def rectangular(ys, h):
    return np.sum(h * np.array(ys[:-1]))
# 复化梯形
def trapezoidal(ys, h):
    return h * (np.sum(np.array(ys[1:-1])) + (ys[0] + ys[-1]) / 2)
# 复化抛物线
def parabolic(ys, h):
    rs = []
    for idx in range(0, int((len(ys) - 1) / 2)):
        rs.append(ys[2 * idx] + 4 * ys[2 * idx + 1] + ys[2 * idx + 2])
    return np.sum(1 / 3 * h * np.array(rs))
if __name__ == '__main__':
    start, stop, num = 0, np.pi, 13001
    dx = np.linspace(start=start, stop=stop, num=num)
    dy = [0] * num
    dy[0] = 1  # 极限sin0/0=1
    dy[1:] = fx(dx[1:])
    h = (1 / (num - 1)) * (stop - start)  # 计算切割步长
    accuracy = 7  # 计算结果保留精度
    r1 = rectangular(ys=dy, h=h)  # 0.9460831
    print('复化矩形算法中，当步长为{}，定积分sin(x)/x在区间[0, pi]的计算结果是：{}'.format(round(h, 4), round(float(r1), accuracy)))
    r2 = trapezoidal(ys=dy, h=h)
    print('复化梯形算法中，当步长为{}，定积分sin(x)/x在区间[0, pi]的计算结果是：{}'.format(round(h, 4), round(float(r2), accuracy)))
    r3 = parabolic(ys=dy, h=h)
    print('复化抛物线算法中，当步长为{}，定积分sin(x)/x在区间[0, pi]的计算结果是：{}'.format(round(h, 4), round(float(r3), accuracy)))
    r4 = monteCarlo(start=start, stop=stop, iter=20)
    print('蒙特卡洛算法中，定积分sin(x)/x在区间[0, pi]的计算结果是：{}'.format(round(float(r4), accuracy)))
    r5 = sci.fixed_quad(fx, start, stop)[0]
    print('固定高斯求积算法中，定积分sin(x)/x在区间[0, pi]的计算结果是：{}'.format(round(r5, accuracy)))
