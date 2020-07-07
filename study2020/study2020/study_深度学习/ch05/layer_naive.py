class Mullayer:
    '''
    乘法层实现
    '''
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self,x,y):
        self.x = x
        self.y = y
        out = x*y

        return out

    def backward(self,dout):
        dx = dout * self.y #翻转x和y
        dy = dout * self.x

        return dx,dy

class AddLayer:
    def __init__(self):
        pass

    def forward(self,x,y):
        out = x+y

        return out

    def backward(self,dout):
        dx = dout*1
        dy = dout*1

        return dx,dy


def two_apple():
    '''测试买苹果的乘法层'''
    apple = 100
    apple_num = 2
    tax = 1.1
    # layer
    mul_appe_layer = Mullayer()
    mul_tax_layer = Mullayer()

    # forward
    apple_price = mul_appe_layer.forward(apple, apple_num)
    price = mul_tax_layer.forward(apple_price, tax)
    print(int(price))
    # backward
    dprice = 1
    dapple_price, dtax = mul_tax_layer.backward(dprice)
    dapple, dapple_num = mul_appe_layer.backward(dapple_price)

    print(dapple, int(dapple_num), dtax)


def two_apple_and_three_orange():
    apple = 100
    apple_num = 2
    orange = 150
    orange_num = 3
    tax = 1.1

    #layer
    mul_apple_layer = Mullayer()
    mul_orange_layer = Mullayer()
    add_apple_orange_layer = AddLayer()
    mul_tax_layer = Mullayer()

    #forward
    apple_price = mul_apple_layer.forward(apple,apple_num)
    orange_price = mul_orange_layer.forward(orange,orange_num)
    all_price = add_apple_orange_layer.forward(apple_price,orange_price)
    price = mul_tax_layer.forward(all_price,tax)
    print(price)

    #backward
    dout = 1
    dall_price,dtax = mul_tax_layer.backward(dout)
    dapple_price,dorange_price = add_apple_orange_layer.backward(dall_price)
    dorange,dorange_num = mul_orange_layer.backward(dorange_price)
    dapple,dapple_num = mul_apple_layer.backward(dapple_price)

    print(dapple_num,dapple,dorange_num,dorange,dtax)

if __name__=='__main__':
    two_apple()
    two_apple_and_three_orange()



