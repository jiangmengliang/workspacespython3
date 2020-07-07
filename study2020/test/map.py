# -*- coding:utf-8 -*-
#!/usr/bin/env python
# @author: jiang.ml
# @time: 2019-09-18 16:10
import numpy as np
from matplotlib import pyplot as plt
# import matplotlib
#新增加的两行
# import matplotlib
# matplotlib.rc("font",family='YouYuan')

# plt.rcParams['font.family'] = ['Times New Roman']
# plt.rcParams['font.family'] = ['YouYuan']
plt.rcParams.update({'font.size': 8})
plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号

x = np.array([1,2,3,4,5])
y = np.array([1,4,9,16,25])

plt.ylabel("y轴")
plt.title(u"s名称")
plt.plot(x,y)
plt.show()

