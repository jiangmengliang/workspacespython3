# -*- coding:utf-8 -*-
#!/usr/bin/env python
# @author: jiang.ml
# @time: 2019-09-23 17:15
from datetime import datetime as dt
import time
import pandas as pd
import numpy as np
"""
dfname._stat_axis.values.tolist()  # 行名称

dfname.columns.values.tolist()  # 列名

"""

# result_df = pd.DataFrame([[1,2,3],[4,5,6]])
# for index in result_df._stat_axis.values.tolist() :
# 	for col in result_df.columns.values.tolist():
# 		print(str(index)+"-----"+str(col))
# 		print(result_df.iloc[index,col])
#
# start_time = dt.now()
# time.sleep(10)
# end_time = dt.now()
# print(end_time - start_time)



# a = ['0'+str(i)+'月' for i in range(3,10)]
# b = list()
# for i in range(3,10):
# 	a = ['0'+str(i)+'月']*15
# 	b.extend(a)
# b.extend(['10月']*15)
# b.extend(['11月']*15)
# b.extend(['12月']*15)
# b.extend(['01月']*15)
# b.extend(['02月']*15)
# print(b)
#
# start_time = dt.now()
# print(start_time)
#
# time.strftime("%Y", time.localtime(time.time()-3*365*24*60*60))

# b = list()
# for i in range(3,10):
# 	a = ['0'+str(i)+'月']*15
# 	b.extend(a)
# b.extend(['10月']*15)
# b.extend(['11月']*15)
# b.extend(['12月']*15)
# b.extend(['01月']*15)
# b.extend(['02月']*15)
# c = ['15及之前','2016','2016','2016','2016','2017','2017','2017','2017','2018','2018','2018','2018','2019','2019']*12
#
# d = ['15及之前','春','夏','秋','冬','春','夏','秋','冬','春','夏','秋','冬','春','夏']*12
# print(d)
# result = list()
# result.append(b)
# result.append(c)
# result.append(d)
# result_df = pd.DataFrame(result)
# result_df_t = result_df.T
# print(result_df)

# b = list()
# for i in range(3, 10):
# 	a = ['0' + str(i)] * 15
# 	b.extend(a)
# b.extend(['10'] * 15)
# b.extend(['11'] * 15)
# b.extend(['12'] * 15)
# b.extend(['01'] * 15)
# b.extend(['02'] * 15)
# c = ['15及之前', '2016', '2016', '2016', '2016', '2017', '2017', '2017', '2017', '2018', '2018', '2018', '2018',
#      '2019', '2019'] * 12
# d = ['15及之前', '春', '夏', '秋', '冬', '春', '夏', '秋', '冬', '春', '夏', '秋', '冬', '春', '夏'] * 12
# e = list()
# e.append(b)
# e.append(c)
# e.append(d)
# template = pd.DataFrame(e).T
# print(template)

# a = {"a":[1,2,3,4],
#      "b":['a','b','c','d']}
#
# b = {"a":[1,2,3],
#      "d":['A','B','C']}
#
# aa = pd.DataFrame(a)
# bb = pd.DataFrame(b)
# c = pd.merge(aa,bb,how='left')
#
# print(c)
#
#
# print("1234.json"[:-1])
#
#
# c.columns = [str(i) for i in range(c.shape[1]) ]
#
# print(c)
#
#
# s = pd.DataFrame([[1,2,3],[1,2,3],[1,2,3]],[1,4,5])
# print(s)
# x = []
# no_data_columns = list(set(range(10)) )
# print(no_data_columns)
# df_empty = pd.DataFrame(columns=[i for i in range(10)])
#
# df_result = df_empty.append(s, ignore_index=True)
# print(df_result)

merge_df = pd.DataFrame([['a','b','c','a','a'],['a',2,3,1,1],["A",'B','C','A','A']],columns=['one','two','three','four','five'])
# merge_df.loc[merge_df["7"] == self.brand_code]
merge_df = merge_df.loc[merge_df['one']=='a']
print(merge_df)



