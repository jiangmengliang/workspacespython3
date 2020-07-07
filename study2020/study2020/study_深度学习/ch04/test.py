import sys,os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True,one_hot_label=True )
print(x_train.shape)
print(t_train.shape)
train_size = x_train.shape[0]
print(train_size)
batch_size = 10
batch_mask = np.random.choice(train_size,batch_size)
print(batch_mask)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]

def cross_entropy_error(y,t): #对应的one-hot t为[0,0,1,0,0,0,0..]这种形式
    if y.ndim == 1:
        t = t.reshape(1,t.size)
        y = y.reshape(1,y.size)
    batch_size = y.shape[0]
    return -np.sum(t*np.log(y + 1e-7))/batch_size

def cross_entropy_error(y,t): #对应的是非one-hot,t为标签 2，7
    if y.ndim == 1:
        t = t.reshape(1,t.size)
        y = y.reshape(1,y.size)
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size),t] + 1e-7))/batch_size

def numerical_diff(f,x):#求导——数值微分
    h = 1e-4 #0.0001
    return (f(x+h)-f(x-h))/(2*h)


def funcation_1(x):
    return 0.01*x**2+0.1*x

#画图代码
import matplotlib.pylab as plt
x = np.arange(0.0,20.0,0.1)
y = funcation_1(x)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

print(numerical_diff(funcation_1,5))
print(numerical_diff(funcation_1,10))

