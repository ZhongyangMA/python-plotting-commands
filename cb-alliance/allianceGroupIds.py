# -*- coding: utf-8 -*-
import math
import csv
import time

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from scipy.optimize import curve_fit

allianceGroupIds = csv.reader(open('../data/alliance158groupIds.csv', encoding='utf-8'))
lineNum = 0
calls_arr = []
rate_arr = []
groupNum1000 = 0
callsSum1000 = 0
callsSumTotal = 0
rate065Count = 0
rate065CallSum = 0
for row in allianceGroupIds:
    lineNum += 1
    if (lineNum == 1):
        continue
    print("groupId=", row[0])
    print("calls=", row[2])
    calls_arr.append(float(row[2]))
    print("rate=", row[3])
    rate_arr.append(float(row[3]))
    if float(row[2]) > 323:
        groupNum1000 += 1
        callsSum1000 += float(row[2])
    callsSumTotal += float(row[2])
    if float(row[3]) > 0.65:
        rate065Count += 1
        rate065CallSum += float(row[2])
print("lineNum=", lineNum)

plt.figure("图1", figsize=(12, 4))  # 创建一个图文件
# 第一个子图
plt.subplot(1, 3, 1)  # 创建第一个子panel (行,列,第几个图)
plt.title("Calls Distribution")
plt.xlabel('calls')  # x坐标轴标题
plt.ylabel('Num.')      # y坐标轴标题
plt.yscale('log')  ## 设置y轴为对数轴
plt.axis([-100, 6000, 0.8, 200])  # 设定坐标轴范围[xmin, xmax, ymin, ymax]
n_calls, bins_calls, patches_calls = plt.hist(calls_arr, bins=30)
plt.vlines([5300], 0, 2, linestyles='dashed', color='red', linewidth=1)  # 竖直方向虚线网格([x1,x2,...], ymin, ymax)
plt.text(4650, 2.5, 'gid:1624', fontsize=10, color='red')
plt.vlines([1000], 0, 1000, linestyles='dashed', color='purple', linewidth=1)  # 竖直方向虚线网格([x1,x2,...], ymin, ymax)
print("groupNum1000=", groupNum1000)
print("groupNum percent=", groupNum1000 / (lineNum - 1))
print("callsSum1000=", callsSum1000)
print("callsSum percent=", callsSum1000 / callsSumTotal)
plt.text(1100, 30, '> 1000', fontsize=10, color='purple')
plt.text(1100, 20, 'gids 3.2%', fontsize=10, color='purple')
plt.text(1100, 15, 'calls 52.9%', fontsize=10, color='purple')
# 拟合指数分布
def func(x, a, b, c):
    return a * np.exp(b * x) + c

y_exp_line = [func(i, 212.1, -0.0097, 0.9543) for i in bins_calls]
plt.plot(bins_calls, y_exp_line, 'r--')

#popt, pcov = curve_fit(func, bins_calls, n_calls)
#print("a=", popt[0])
#print("b=", popt[1])
#y_exp_line = [func(i, popt[0], popt[1], popt[2]) for i in bins_calls]
#plt.plot(bins_calls, y_exp_line, 'r--')

# 第二个子图
plt.subplot(1, 3, 2)  # 创建第二个子panel (行,列,第几个图)
plt.title("Rate Distribution")
plt.xlabel('rate')  # x坐标轴标题
plt.ylabel('Num.')      # y坐标轴标题
plt.axis([-0.1, 1.1, 0, 30])  # 设定坐标轴范围[xmin, xmax, ymin, ymax]
plt.hist(rate_arr, bins=30)
plt.vlines([0.8925], 0, 30, linestyles='dashed', color='red', linewidth=1)  # 竖直方向虚线网格([x1,x2,...], ymin, ymax)
plt.text(0.65, 20, 'gid:1624', fontsize=10, color='red')

# 第三个子图
plt.subplot(1, 3, 3)  # 创建第三个子panel (行,列,第几个图)
plt.title("Rate vs. Calls")
plt.xlabel('calls')  # x坐标轴标题
plt.ylabel('rate')      # y坐标轴标题
plt.axis([0.6, 10000, -0.1, 1.1])  # 设定坐标轴范围[xmin, xmax, ymin, ymax]
plt.xscale('log')
plt.scatter(calls_arr, rate_arr)
plt.scatter([5375.75], [0.8925], color='red')
plt.text(4550, 0.8, '1624', fontsize=10, color='red')
plt.hlines([0.65, 0.65], 0, 10000, linestyles='dotted', linewidth=0.8, color='blue')  # 水平方向虚线网格([y1,y2,...], xmin, xmax)
plt.text(1000, 0.6, 'rate 0.65', fontsize=10, color='blue')
print("rate065Count=", rate065Count)
print("rate065Count percent=", rate065Count / (lineNum - 1))
print("rate065CallSum=", rate065CallSum)
print("rate065CallSum percent=", rate065CallSum / callsSumTotal)

plt.show()

u=10
v=15
sigma = math.sqrt(1 / u + 1 / v)
print("sigma=", sigma)
