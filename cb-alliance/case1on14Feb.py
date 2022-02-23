# -*- coding: utf-8 -*-
import math
import csv
import time

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

case1on214 = csv.reader(open('../data/case1on214.csv', encoding='utf-8'))
numOfline = 0
time_arr_total = []
time_arr_timeout = []
time_arr_succ = []
for row in case1on214:
    numOfline += 1
    if (numOfline == 1):
        continue
    timestamp = time.mktime(time.strptime(row[0], "%Y-%m-%dT%H:%M:%S.000+08:00"))  # timestamp in seconds
    time_arr_total.append(timestamp)
    timeoutFlag = 0
    if (row[8] == "timeout"):  # status
        timeoutFlag = 1
        time_arr_timeout.append(timestamp)
    else:
        time_arr_succ.append(timestamp)
    print("timestamp in seconds: ", timestamp)
    print("timeout flag: ", timeoutFlag)

time_arr_timeout.append(time_arr_total[0])
print("lines = ", numOfline)

plt.figure("图1", figsize=(8, 8))  # 创建一个图文件
# 第一个子图
plt.subplot(2, 1, 1)  # 创建第一个子panel (行,列,第几个图)
plt.title("Check Avail")
plt.xlabel('timestamp in seconds')  # x坐标轴标题
plt.ylabel('Num.')      # y坐标轴标题
plt.axis([1644822098, 1644832221, 0, 20])  # 设定坐标轴范围[xmin, xmax, ymin, ymax]
plt.hist(time_arr_total, bins=100, color='blue', ec='black', alpha=1)  # 直方图 color填充颜色 ec包络线颜色
plt.hist(time_arr_timeout, bins=100, color='red', ec='black', alpha=0.9)  # 直方图 color填充颜色 ec包络线颜色
plt.legend(["成功数", "超时数"])

# 第二个子图
plt.subplot(2, 1, 2)  # 创建第二个子panel (行,列,第几个图)
plt.xlabel('timestamp in seconds')  # x坐标轴标题
plt.ylabel('Failure Rate per 5 mins')      # y坐标轴标题
plt.axis([1644822098, 1644832221, 0, 1.2])  # 设定坐标轴范围[xmin, xmax, ymin, ymax]

n, bins, patches = plt.hist(time_arr_total, bins=30, alpha=0)  # 直方图 color填充颜色 ec包络线颜色
n1, bins1, patches1 = plt.hist(time_arr_timeout, bins=30, alpha=0)  # 直方图 color填充颜色 ec包络线颜色

time_arr = []
rate_arr = []
rate_err_arr = []
for i in range(len(n)):
    time_arr.append(bins[i])
    rate_arr.append(n1[i] / n[i])
    rate_err_arr.append(math.sqrt(1/n1[i] + 1/n[i]))  # 泊松误差

plt.plot(time_arr, rate_arr, 'mo:')
plt.errorbar(time_arr, rate_arr, yerr=rate_err_arr, fmt='mo:', linewidth=0.8, capsize=3)  # capsize 误差棒短线的长度

# 绘制嵌入图
plt.axes([0.2, 0.25, 0.2, 0.15])  # [左,下,宽,高] 相对于整个figure
plt.title('5mins计数分布')
plt.axis([-10, 50, 0, 0.07])  # 设定坐标轴范围[xmin, xmax, ymin, ymax]
n_n, bins_n, patches_n = plt.hist(n, bins=10, density=True, color='cyan', ec='black')  # n的分布
mu = np.mean(n)    # 均值
sigma = np.std(n)  # 标准差
print("mu=", mu)
print("sigma=", sigma)
y_norm = norm.pdf(bins_n, mu, sigma)  # 拟合一条最佳正态分布曲线y_norm
plt.plot(bins_n, y_norm, 'r--')  # 绘制y_norm的曲线






plt.show()
