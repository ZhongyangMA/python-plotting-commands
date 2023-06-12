# -*- coding: utf-8 -*-
import json

import xgboost as xgb

# 数据读取
xgb_train = xgb.DMatrix('demo/data/agaricus.txt.train')
xgb_test = xgb.DMatrix('demo/data/agaricus.txt.test')
print("xgb_train: ", xgb_train)
print("xgb_test: ", xgb_test)

# 定义模型训练参数
params = {
    "objective": "binary:logistic",
    "booster": "gbtree",
    "max_depth": 3
}

# 训练轮数
num_round = 5

# 训练过程中实时输出评估结果
watchlist = [(xgb_train, 'train'), (xgb_test, 'test')]

# 模型训练
model = xgb.train(params, xgb_train, num_round, watchlist)

# 模型预测
preds = model.predict(xgb_test)
print("preds: ", preds)
