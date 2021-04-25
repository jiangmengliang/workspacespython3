# -*- coding:utf-8 -*-
#!/usr/bin/env python
# @author: jiang.ml
# @time: 2019-09-25 15:36
# import pymysql
#
# conn = pymysql.connect(host="0.0.0.0", port=3306,\
#                 user='user', password='password', db='db', charset='utf8')
# cur = conn.cursor()
# cur.execute("show databases")
# x = cur.fetchall()
# print(x)
import pandas as pd
import pymysql
# conn = pymysql.connect(host='10.240.116.22',port=3306,user='user',password='password',db='db',charset='utf8')
# cursor = conn.cursor()
# sql = "insert into test(user,age) values(%s,%s) "
# user = 'jiang'
# age = 25
# data = [("jiang",25),("meng",26),("liang",27)]
# try:
#     # 单条插入数据
#     # cursor.execute(sql,[user,age])
#     # 批量插入数据
#     cursor.executemany(sql,data)
#     conn.commit()
#     print("数据入库完成..........")
# except:
#     conn.rollback()
#     print("数据入库失败.........")
# cursor.close()
# conn.close()



# sql = "update test set age=%s where user=%s"
# user = 'jiang'
# age = 30
# data = [(50,"jiang"),(60,"meng"),(70,"liang")]
# try:
#     #单条更新
#     # cursor.execute(sql,[age,user])
#     #批量更新
#     cursor.executemany(sql,data)
#     conn.commit()
#     print("数据更新完成..........")
# except:
#     conn.rollback()
#     print("数据更新失败.........")
# cursor.close()
# conn.close()

# df = pd.DataFrame([[1,2,3,4],['a','b','c','d']])
# a = df.to_numpy()
# print(a)
# b = [tuple(x) for x in a ]
# print(b)
# df = pd.DataFrame([[1,2,3,4],['a','b','c','d']],columns=['1','3','0','2'])
# print(df)

import pandas as pd
a=["1001","1002","1003"]
b=["xiaoming","xiaohong","xiaohua"]
c=["77","88","99"]
d=["87","82","91"]
dataframe = pd.DataFrame({'number':a,'name':b,'Python':c,'Math':d})
print(dataframe)
order = ['name','Python','Math','number']
dataframe = dataframe[order]
dataframe.to_excel()
print(dataframe)

print([str(i) for i in range(0,10)])

self.detail_query_index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                           26, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                           51, 52, 53, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 72, 73, 74, 75,
                           76, 77, 78, 79, 109, 111, 113, 115, 120, 122, 124, 126, 131, 133, 135, 137, 153, 155, 157,
                           159, 164, 166, 168, 170, 175, 177, 179, 181, 197, 199, 201, 203, 208, 210, 212, 214, 219,
                           221, 223, 225, 241, 243, 245, 247, 252, 254, 256, 258, 263, 265, 267, 269]



