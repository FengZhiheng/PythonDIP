# https://zhuanlan.zhihu.com/p/125744910

#定义函数
def f(x):
    return 0.5 * (x - 0.25)**2


#f(x)的导数(现在只有一元所以是导数，如果是多元函数就是偏导数)
def df(x):
    return x - 0.25 #求导应该不用解释吧

alpha = 1.6 #你可以更改学习率试试其他值


GD_X = [] #每次x更新后把值存在这个列表里面
GD_Y = [] #每次更新x后目标函数的值存在这个列表里面
x = 3 #随机初始化的x,其他的值也可以
f_current = f_change = f(x)
iter_num = 0


while iter_num <= 1000 and f_change > 1e-10:
    iter_num +=1
    x = x - alpha *df(x)
    tmp = f(x)
    f_change = abs(f_current - tmp)
    f_current = tmp
    GD_X.append(x)
    GD_Y.append(f_current)

print(iter_num)

import numpy as np
import matplotlib.pyplot as plt

X = np.arange(-4,4,0.05)
Y = f(X)
Y = np.array(Y)

plt.plot(X,Y)
plt.scatter(GD_X,GD_Y)
plt.title("y = 0.5(x - 0.25)^2")
plt.show()


plt.plot(X,Y)
plt.scatter(GD_X,GD_Y)
plt.title("$y = 0.5(x - 0.25)^2$")
plt.show()