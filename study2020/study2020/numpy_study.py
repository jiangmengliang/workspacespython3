# -*- coding:utf-8 -*-
#!/usr/bin/env python
# @author: jiang.ml
# @time: 2019-09-11 16:21
import importlib,sys
importlib.reload(sys)
import numpy as np
"""numpy中的array的数据类型"""
# dt = np.dtype([('ago',np.int8)])
# print(dt)
# agos = np.array([(20,),(30,),(40,)],dtype=dt)
# print(agos)
# print(agos['ago'])
#
# a = np.arange(24)
# print(a.ndim)
# b = a.reshape(2,3,4)
# print(b)
# print(b.ndim)
#
#
# a = np.array([[1,2,3],[1,2,3]])
# print(a)
# print(a.shape)
# a.shape = (3,2)
# print(a)
#
# a = np.array([[1,2,3],[1,2,3]],np.int8)
# print(a.itemsize)
# a = np.array([[1,2,3],[1,2,3]],np.float64)
# print(a.itemsize)
#
# a = np.array([[1,2,3],[1,2,3]])
# print(a.flags)
#
#
# a = np.empty([3,2],dtype=float,order='C')
# print(a)
#
# a = np.zeros([3,2],dtype=float,order='F')
# print(a)
# print(a.ndim)
# print(a.shape)
# print(a.flags)
#
#
# #array的索引切片
# a = np.arange(1,10)
# b = a[2:7:2]
# print(b)
#
# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a[...,1])
# print(a[: ,1])
# print("-----")
# print(a[1,...])
# print(a[1, :])
# print("--------")
# print(a[...,1:])
# print(a[:,1:])
#
#
# b = np.array([1,2,3])
# bb = np.tile(b, (4, 1))
# print(bb)



"""连接数组"""
# a = np.array([[1,2],[3,4]])
# b = np.array([[5,6],[7,8]])
# # 函数用于沿指定轴连接相同形状的两个或多个数组
# # print(np.concatenate((a,b)))
# # print(np.concatenate((a,b),axis=1))
#
# #  函数用于沿新轴连接数组序列
# # print(np.stack((a,b),axis=0))
# # print(np.stack((a,b),axis=1))
#
# # numpy.hstack 是 numpy.stack 函数的变体，它通过水平堆叠来生成数组。
# print(np.hstack((a,b)))
#
# # numpy.vstack 是 numpy.stack 函数的变体，它通过垂直堆叠来生成数组。
# print(np.vstack((a,b)))

"""数组拆分"""
#
# # np.split拆分数组
# # a = np.array(np.arange(9))
# # print(np.split(a,[4,7]))
#
# # numpy.hsplit用于水平切割数组
# a = np.floor(10*np.random.random((2,6)))
# print(a)
# print("/n/n")
# print(np.hsplit(a,3))
#
# #numpy.vsplit沿着垂直轴分割，其分割方式与hsplit用法相同。
#
# a = np.arange(16).reshape(4,4)
# print(a)
# print(np.vsplit(a,3))

# a = np.array([[1,2,3],[4,5,6]])
#
#
# print(np.append(a,[[7,8,9]],axis=0))
#
#
# print(np.append(a,[[7],[8]],axis=1))


# a = np.array([[1,2],[3,4],[5,6]])
#
# print(np.insert(a,3,[1,2,3]))
#
# print(np.insert(a,3,[11,12],axis=0))
#
#
# print(np.insert(a,2,[11,12,13],axis=1))

"""去重np.unique"""
# a = np.array([5,2,6,2,7,5,6,8,2,9])
# print("第一个去重数组;")
# print(np.unique(a))
# print("\n")
# print("去重数组索引;")
# u,indicex = np.unique(a,return_index=True)
# print(u)
# print(indicex)
# print("\n")
# print("去重数组下标:")
# u,indicex = np.unique(a,return_inverse=True)
# print(u)
# print(indicex)
# print("\n")
# u,indicex = np.unique(a,return_counts=True)
# print(u)
# print(indicex)

"""位运算"""
# a = 13
# b = 17
# print(bin(a), bin(b))
#
# print(np.bitwise_and(a, b))
#
# print(np.bitwise_or(a, b))

"""字符串函数"""
# a = ["hello"]
# b = [" jiang"]
# c = ["hello", "hi"]
# d = [" jiang", " meng"]
#
# print(np.char.add(a, b))
# print(np.char.add(c, d))
#
# print(np.char.multiply('jiang ',3))
#
# print(np.char.center('jiang',20,'*'))
#
# print(np.char.capitalize('jiang'))
#
# print(np.char.title('jiang meng liang'))
#
# print(np.char.lower('JIANG Meng Liang'))
#
# print(np.char.upper('Jiang mENG liang'))
#
# print(np.char.split('jiang.meng.liang','.'))
#
# print(np.char.split('jiang meng liang'))
#
# print(np.char.strip('jiang meng liangj','j'))
#
# print(np.char.strip(['jiang','meng','liang'],'g'))
#
# print(np.char.join([":","-","|"],['jiang','meng','liang']))
#
# print(np.char.replace("jiang meng liang",'ang','123'))
#
# print(np.char.encode("jiang meng liang","cp500"))
#
# print(np.char.decode(b'\x91\x89\x81\x95\x87@\x94\x85\x95\x87@\x93\x89\x81\x95\x87',"cp500"))

"""数学函数"""
# a = np.array([0,30,60,90,180])
#
# print(np.sin(a*np.pi/180))
#
# print(np.cos(a*np.pi/180))
#
# print(np.tan(a*np.pi/180))
#
# a = [1.22,22.33,3.44]
# print(np.around(a,1))
# print(np.around(a,-1))
#
# b = [-1.2,1.2,-2.6,2.8]
# print(np.floor(b))
#
# print(np.ceil(b))
#
# c = [1.5,2,0.25,4]
# print(np.reciprocal(c))
#
# d = [1,10,20]
# f = [2,3,4]
# print(np.power(d,f))

"""排序"""
# a = np.array([[3,7],[9,1]])
# print(np.sort(a))
#
# print(np.sort(a,axis=0))
#
# print(np.sort(a,axis=1))
#
# a = np.array([[30,40,0],[0,20,10],[50,0,60]])
#
# print(np.nonzero(a))
#
# x = np.arange(9.).reshape(3,  3)
# a = np.where(x > 3)
# print(a)
# print("\n")
# print(x[a])
#
# condition = np.mod(x,2) == 0
# print(condition)
# print(np.extract(condition,x))

"""矩阵"""
# import numpy.matlib as mt
# print (mt.empty((2,2)))
#
# print(mt.zeros([2,2]))
#
# print(mt.ones([2,2]))
#
# print(mt.eye(n=3,M=4,k=1,dtype=float))
#
#
# print(mt.identity(5,dtype=float))
#
#
# print(mt.rand(2,3))

"""IO"""
arr = np.array([[1,2,3],[3,4,5]])
np.save('outfile.npy',arr)
np.save('outfile2',arr)

b = np.load("outfile.npy")
print(b)