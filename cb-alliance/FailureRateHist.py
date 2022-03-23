# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import json

# Vendor
switch_vendor = json.load(open('../data/switch-vendor.json', encoding='utf-8'))
vendor_threshold = 0.30
vendor_total_arr = []
vendor_above_arr = []
vendor_below_arr = []
for item in switch_vendor:
    source = item['_source']
    failureRate = float(source['incidentID'])
    vendor_total_arr.append(failureRate)
    if failureRate > vendor_threshold:
        vendor_above_arr.append(failureRate)
    else:
        vendor_below_arr.append(failureRate)

print("vendor total count: " + str(len(vendor_total_arr)) + ", mean: " + str(np.mean(vendor_total_arr)))
print("vendor below count: " + str(len(vendor_below_arr)) + ", mean: " + str(np.mean(vendor_below_arr)))
print("vendor above count: " + str(len(vendor_above_arr)))

# Hotel
switch_hotel = json.load(open('../data/switch-hotel.json', encoding='utf-8'))
hotel_threshold = 0.40
hotel_total_arr = []
hotel_above_arr = []
hotel_below_arr = []
for item in switch_hotel:
    source = item['_source']
    failureRate = float(source['incidentID'])
    hotel_total_arr.append(failureRate)
    if failureRate > hotel_threshold:
        hotel_above_arr.append(failureRate)
    else:
        hotel_below_arr.append(failureRate)

print("hotel total count: " + str(len(hotel_total_arr)) + ", mean: " + str(np.mean(hotel_total_arr)))
print("hotel below count: " + str(len(hotel_below_arr)) + ", mean: " + str(np.mean(hotel_below_arr)))
print("hotel above count: " + str(len(hotel_above_arr)))

# 绘图
plt.figure("图1", figsize=(12, 6))  # 创建一个图文件
# 第1个子图
plt.subplot(1, 2, 1)  # 创建第1个子panel (行,列,第几个图)
plt.title("CB-Alliance Vendor维度失败率分布")
plt.xlabel('Failure Rate')        # x坐标轴标题
plt.ylabel('Num.')  # y坐标轴标题
plt.axis([0, 1, 0, 100])  # 设定坐标轴范围[xmin, xmax, ymin, ymax]
plt.hist(vendor_total_arr, bins=30)

plt.text(vendor_threshold + 0.02, 80, '%.2f' % np.mean(vendor_threshold), fontsize=10, color='red')
plt.vlines([vendor_threshold], 0, 100, color='red', linestyles='dashed')  # 竖直方向虚线网格([x1,x2,...], ymin, ymax)
plt.text(0.28, 61, '%.2f' % np.mean(vendor_total_arr), fontsize=10, color='blue')
plt.vlines([np.mean(vendor_total_arr)], 0, 60, color='blue', linewidth=2)  # 竖直方向虚线网格([x1,x2,...], ymin, ymax)
plt.text(np.mean(vendor_below_arr) - 0.05, 61, '%.2f' % np.mean(vendor_below_arr), fontsize=10, color='green')
plt.vlines([np.mean(vendor_below_arr)], 0, 60, color='green', linewidth=2)  # 竖直方向虚线网格([x1,x2,...], ymin, ymax)
plt.legend(["threshold", "mean(total)", "mean(below)"])

# 第2个子图
plt.subplot(1, 2, 2)  # 创建第2个子panel (行,列,第几个图)
plt.title("CB-Alliance Hotel维度失败率分布")
plt.xlabel('Failure Rate')        # x坐标轴标题
plt.ylabel('Num.')  # y坐标轴标题
plt.axis([0, 1, 0, 100])  # 设定坐标轴范围[xmin, xmax, ymin, ymax]
plt.hist(hotel_total_arr, bins=30)

plt.text(hotel_threshold + 0.02, 80, '%.2f' % np.mean(hotel_threshold), fontsize=10, color='red')
plt.vlines([hotel_threshold], 0, 100, color='red', linestyles='dashed')  # 竖直方向虚线网格([x1,x2,...], ymin, ymax)
plt.text(0.55, 61, '%.2f' % np.mean(hotel_total_arr), fontsize=10, color='blue')
plt.vlines([np.mean(hotel_total_arr)], 0, 60, color='blue', linewidth=2)  # 竖直方向虚线网格([x1,x2,...], ymin, ymax)
plt.text(np.mean(hotel_below_arr) - 0.05, 61, '%.2f' % np.mean(hotel_below_arr), fontsize=10, color='green')
plt.vlines([np.mean(hotel_below_arr)], 0, 60, color='green', linewidth=2)  # 竖直方向虚线网格([x1,x2,...], ymin, ymax)
plt.legend(["threshold", "mean(total)", "mean(below)"])


plt.show()
