# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import math

plt.figure("图1", figsize=(12, 6))  # 创建一个图文件
# 第一个子图
plt.subplot(1, 2, 1)  # 创建第一个子panel (行,列,第几个图)
plt.title("泊松比率传递误差")
plt.xlabel('total count')        # x坐标轴标题
plt.ylabel('propagation sigma')  # y坐标轴标题
plt.axis([0, 100, 0, 2])  # 设定坐标轴范围[xmin, xmax, ymin, ymax]

total = np.linspace(1, 100, 100)

def sigma(total, rate):
    return math.sqrt(1 / (rate * total) + 1 / total)

sigma_min = [sigma(item, 1) for item in total]
sigma_20 = [sigma(item, 0.2) for item in total]

plt.plot(total, sigma_min, color='red')
plt.plot(total, sigma_20, color='blue')

plt.text(10, 0.2, '失败率100%', fontsize=10, color='red')
plt.text(20, 0.7, '失败率20%', fontsize=10, color='blue')

# 第2个子图
plt.subplot(1, 2, 2)  # 创建第2个子panel (行,列,第几个图)
plt.title("rate-sigma vs. rate")
plt.xlabel('rate')        # x坐标轴标题
plt.ylabel('rate-sigma')  # y坐标轴标题
plt.axis([0, 1, -3, 1])  # 设定坐标轴范围[xmin, xmax, ymin, ymax]
rate = np.linspace(0, 1, 100)
# 四条线
yy20 = [item - sigma(20, item) for item in rate]
plt.plot(rate, yy20, color='red')
yy10 = [item - sigma(10, item) for item in rate]
plt.plot(rate, yy10, color='green')
yy5 = [item - sigma(5, item) for item in rate]
plt.plot(rate, yy5, color='blue')
yy1 = [item - sigma(1, item) for item in rate]
plt.plot(rate, yy1, color='cyan')
plt.legend(["count=20", "count=10", "count=5", "count=1"])

plt.vlines([0.2], -5, 2, linestyles='dashed', color='purple', linewidth=1)  # 竖直方向虚线网格([x1,x2,...], ymin, ymax)
plt.hlines([-0.34, -0.34], 0, 1, linestyles='dashed', linewidth=1, color='purple')  # 水平方向虚线网格([y1,y2,...], xmin, xmax)
plt.scatter([0.2], [-0.34], color='red')
plt.text(0.5, -0.5, 'threshold = -0.34', fontsize=10, color='purple')

plt.show()
