import sys,os
import numpy as np
sys.path.append(os.pardir)
from dataset.mnist import load_mnist
from two_layer_net import TwoLayerNet
import matplotlib.pyplot as plt

(x_train,t_train),(x_test,t_test) = load_mnist(flatten=True,one_hot_label=True)

train_loss_list = []

#超参数
iters_num = 10000
train_size = x_train.shape[0]
batch_size = 100
learning_rate = 0.1
network = TwoLayerNet(input_size=784,hidden_size=50,output_size=10)

for i in range(iters_num):
    #获取mini_batch
    batch_mask = np.random.choice(train_size,batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]

    #计算梯度
    grad = network.numerical_gradient(x_batch,t_batch)
    # grad = network.numerical_gradient(x_batch,t_batch) #高速版

    #更新参数
    for key in('W1','b1','W2','b2'):
        network.params[key] -= learning_rate*grad[key]

    #记录学习过程
    loss = network.loss(x_batch,t_batch)
    train_loss_list.append(loss)


markers = {'train': 'o', 'test': 's'}
x = np.arange(len(train_loss_list))
plt.plot(x, train_loss_list, label='train loss')
# plt.plot(x, train_loss_list, label='test acc', linestyle='--')
plt.xlabel("loss")
plt.ylabel("item")
# plt.ylim(0, 1.0)
# plt.legend(loc='lower right')
plt.show()