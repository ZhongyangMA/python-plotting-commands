# -*- coding: utf-8 -*-
import csv
import matplotlib.pyplot as plt
import numpy as np

import matplotlib
print(matplotlib.matplotlib_fname())  # 查找字体路径

score_arr_total = []
score_arr_meet = []
num_total = 0
num_meet = 0
num_total_1 = 0
num_total_2 = 0
num_total_3 = 0
num_total_4 = 0
num_total_5 = 0
num_meet_1 = 0
num_meet_2 = 0
num_meet_3 = 0
num_meet_4 = 0
num_meet_5 = 0
c1_clues = csv.reader(open('data/xxx.txt', encoding='utf-8'))
for row in c1_clues:
    print(row)
    # total
    if(float(row[2]) > 1 and float(row[2]) < 99):
        score_arr_total.append(float(row[2]))
        num_total += 1
        if(int(row[3]) > 0):
            score_arr_meet.append(float(row[2]))
            num_meet += 1
    # bins
    if(float(row[2]) > 1 and float(row[2]) <= 16):
        num_total_1 += 1
        if(int(row[3]) > 0):
            num_meet_1 += 1
    if(float(row[2]) > 16 and float(row[2]) <= 30):
        num_total_2 += 1
        if(int(row[3]) > 0):
            num_meet_2 += 1
    if(float(row[2]) > 30 and float(row[2]) <= 50):
        num_total_3 += 1
        if(int(row[3]) > 0):
            num_meet_3 += 1
    if(float(row[2]) > 50 and float(row[2]) < 67):
        num_total_4 += 1
        if(int(row[3]) > 0):
            num_meet_4 += 1
    if(float(row[2]) > 67 and float(row[2]) < 99):
        num_total_5 += 1
        if(int(row[3]) > 0):
            num_meet_5 += 1

# 关键变量
print("num_total = ", num_total)
print("num_total_1 = ", num_total_1)
print("num_total_2 = ", num_total_2)
print("num_total_3 = ", num_total_3)
print("num_total_4 = ", num_total_4)
print("num_total_5 = ", num_total_5)
print("num_meet = ", num_meet)
print("num_meet_1 = ", num_meet_1)
print("num_meet_2 = ", num_meet_2)
print("num_meet_3 = ", num_meet_3)
print("num_meet_4 = ", num_meet_4)
print("num_meet_5 = ", num_meet_5)

meet_ratio = 1.0*num_meet/num_total  # 平均转化率
print("meet_ratio = ", meet_ratio)

meet_ratio_arr = [1.0*num_meet_1/num_total_1, 1.0*num_meet_2/num_total_2, 1.0*num_meet_3/num_total_3, 1.0*num_meet_4/num_total_4, 1.0*num_meet_5/num_total_5]
print("meet_ratio_arr = ", meet_ratio_arr)
meet_ratio_error_arr = [np.sqrt(1.0/num_meet_1 + 1.0/num_total_1), np.sqrt(1.0/num_meet_2 + 1.0/num_total_2), np.sqrt(1.0/num_meet_3 + 1.0/num_total_3), np.sqrt(1.0/num_meet_4 + 1.0/num_total_4), np.sqrt(1.0/num_meet_5 + 1.0/num_total_5)]
print("meet_ratio_error_arr = ", meet_ratio_error_arr)

# 下面开始画图
plt.figure("图1", figsize=(6.5, 6.5))  # 创建一个图文件
# 第一个子图
plt.subplot(2, 1, 1)  # 创建第一个子panel (行,列,第几个图)
plt.title("图的大标题")
plt.xlabel('xxxx')  # x坐标轴标题
plt.ylabel('yyyy')      # y坐标轴标题
plt.axis([0, 100, 0, 300000])  # 设定坐标轴范围[xmin, xmax, ymin, ymax]
# plt.yscale('log')  ## 设置y轴为对数轴
plt.vlines([16, 30, 50, 67], 0, 1.e8, linestyles='dashed', linewidth=0.8)  # 竖直方向虚线网格([x1,x2,...], ymin, ymax)
plt.text(82, 2.5e5, '红：xx数', fontsize=10, color='red')
plt.text(82, 2.2e5, '蓝：xx数', fontsize=10, color='blue')
plt.text(6, 2.8e5, '19.0%       21.0%         20.4%          20.4%             19.1%')

plt.hist(score_arr_total, bins=25, color='red', ec='black')  # 直方图 color填充颜色 ec包络线颜色
plt.hist(score_arr_meet, bins=25, color='blue', ec='black')  # 直方图 color填充颜色 ec包络线颜色

# 第二个子图
plt.subplot(2, 1, 2)  # 创建第二个子panel (行,列,第几个图)
plt.xlabel('xxxx')       # x坐标轴标题
plt.ylabel('yyyy')       # y坐标轴标题
plt.axis([0, 100, 0, 0.5])  # 设定坐标轴范围[xmin, xmax, ymin, ymax]
plt.vlines([16, 30, 50, 67], 0, 1, linestyles='dashed', linewidth=0.8)  # 竖直方向虚线网格([x1,x2,...], ymin, ymax)
plt.hlines(meet_ratio, 0, 100, linestyles='dotted', linewidth=0.8, color='blue')  # 水平方向虚线网格([y1,y2,...], xmin, xmax)
plt.text(72, 0.2, 'average = -0.184', color='blue')
xx = [10, 23, 40, 59, 78]
# plt.plot(xx, meet_ratio_arr, 'mo:')
plt.errorbar(xx, meet_ratio_arr, yerr=meet_ratio_error_arr, fmt='mo:', linewidth=0.8, capsize=3)  # capsize 误差棒短线的长度

plt.show()



