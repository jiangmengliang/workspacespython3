"""简单的神经网络为例，来实现求梯度的代码"""
import sys,os
sys.path.append(os.pardir)
import numpy as np
from common.functions import softmax,cross_entropy_error #softmax函数（）,交叉熵误差（）
from common.gradient import numerical_gradient

class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2,3) #用高斯分布进行初始化

    def predict(self,x):
        return np.dot(x,self.W) #np.dot() 是矩阵相乘

    def loss(self,x,t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y,t)

        return loss




if __name__=='__main__':
    net = simpleNet()
    print(net.W)     #权重

    x = np.array([0.6,0.9]) #输入
    p = net.predict(x) #经历权重的结果值
    print(p)

    print(np.argmax(p)) #最大值索引

    t = np.array([0,0,1]) #正确解标签
    print(net.loss(x,t)) # 交叉熵误差,判断误差大小

    def f(W):
        return net.loss(x,t)

    dW = numerical_gradient(f,net.W) #梯度/导数 =  损失函数，参数
    print(dW)

    f1 = lambda w:net.loss(x,t) #简单的函数可以用lambda定义




