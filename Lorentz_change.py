'''
洛伦兹方程
在惯性坐标系S中，有两个事件同时发生，且在x方向上相距1000m，
从另一个惯性坐标系S'中观察这两个事件在x方向上相距2000m，
求在S'系测得这两个事件发生的时间间隔是多少？
'''
import numpy as np
c = 3.0 * 10 ** 8  # 根据狭义相对论的基本假设，光速是物质的极限速度，不受惯性坐标系影响
# 洛伦兹方程计算在S1中两个事件发生的距离间隔
def Lorentz_change_calc_dx(v, x1, x2, t1, t2):
    return ((x2 - x1) - v * (t2 - t1)) * calc_gama(bate=calc_bate(v))
# 洛伦兹方程计算在S1中两个事件发生的时间间隔
def Lorentz_change_calc_dt(v, x1, x2, t1, t2):
    return ((t2 - t1) - (v / c**2) * (x2 - x1)) * calc_gama(bate=calc_bate(v))
# 从S1中两个事件发生的相隔距离来反向求出v，需要解一元二次方程的根
def Lorentz_change_calc_v_from_dx(x1, x2, x1_, x2_, t1, t2):
    A = ((t1 - t2) / (x2_ - x1_))**2 * c**2 + 1
    B = -2 * c**2 * (((x2 - x1) * (t2 - t1)) / ((x2_ - x1_)**2))
    C = c**2 * (((x2 - x1) / (x2_ - x1_))**2 - 1)
    deta = B**2 - 4 * A * C  # 判断一元二次方程的根是否存在
    if deta > 0:
        ret1 = (-B + deta**0.5) / (2 * A)  # 求根公式
        ret2 = (-B - deta ** 0.5) / (2 * A)
        return np.max([ret1, ret2])
    elif deta == 0:
        return (-B + 0) / (2 * A)
    else:
        print('v的计算存在虚数根！')
        return None
# 计算常量beta
def calc_bate(v):
    return v / c
# 计算常量gama
def calc_gama(bate):
    return 1 / (1 - bate ** 2)**0.5
if __name__ == '__main__':
    x1 = 0.0  # 参考系S中的第一个事件位置
    x2 = 1.0 * 10**3  # 参考系S中的第二个事件位置
    x1_ = 0.0  # 参考系S1中的第一个事件位置
    x2_ = 2.0 * 10**3  # 参考系S1中的第二个事件位置
    t1 = 0.0  # 参考系S中的第一个事件发生的时间
    t2 = 0.0  # 参考系S中的第二个事件发生的时间
    v = Lorentz_change_calc_v_from_dx(x1, x2, x1_, x2_, t1, t2)
    if v is not None:
        dx = Lorentz_change_calc_dx(v, x1, x2, t1, t2)
        dt = Lorentz_change_calc_dt(v, x1, x2, t1, t2)
        print('S1参考系沿着X轴移动的移动速度为：{0}'.format(format(v, '.2e')))
        print('S1参考系的移动速度达到光速的：{0}倍'.format(v / c))
        print('验证在参考系S1中观察到这两个事件的距离为：{0}'.format(dx))
        print('在参考系S1中观察到这两个事件的时间间隔为：{0}'.format(format(abs(dt), '.2e')))
