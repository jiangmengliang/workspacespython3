import numpy as np
x = np.array([0,1]) #输入
w = np.array([0.5,0.5]) #权重
b = -0.7 #偏置
# print(np.sum(x*w)+b)


def AND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7
    tmp = np.sum(x*w)+b
    if tmp<=0:
        return 0
    else:
        return 1

def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    b = 0.7
    tmp = np.sum(x*w) + b
    if tmp<=0:
        return 0
    else:
        return 1

def OR(x1,x2):
    x = np.array([x1, x2])
    w = np.array([0.5,0.5])
    b = -0.1
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1,x2):
    s1 = OR(x1,x2)
    s2 = NAND(x1,x2)
    result = AND(s1,s2)
    return result

print(XOR(0,0))
print(XOR(1,0))
print(XOR(0,1))
print(XOR(1,1))
