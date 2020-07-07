#抽象类加抽象方法就等于面向对象编程中的接口
#python中的类继承
from abc import abstractclassmethod,ABCMeta
class Animal():
    __metaclass__=ABCMeta#经典类---多继承按照"深度优先方式"查找
    @abstractclassmethod  #这些是检查子类是否按照父类的方法名称来写的,并且添加这个，这个eat方法必须被子类重写
    def eat(self):
        print("%s 吃"%self.name)
    def drink(self):
        print("%s 喝"%self.name)
    def shit(self):
        print("%s 拉"%self.name)
    def pee(self):
        print("%s 撒"%self.name)

class Person(object): #新式类--多继承按照"广度优先方式"查找
    def eat(self):
        print("%s 吃"%self.name)
    def drink(self):
        print("%s 喝"%self.name)
    def shit(self):
        print("%s 拉"%self.name)
    def pee(self):
        print("%s 撒"%self.name)

class Cat(Animal):
    def __init__(self,name):
        self.name = name
        self.breed = '喵'
    def cry(self):
        print("喵喵叫")
    def eat(self):
        print("%s喜欢吃鱼"%self.name)


class Dog(Animal):
    def __init__(self,name):
        self.name = name
        self.breed = '汪'
    def cry(self):
        print("汪汪叫")


if __name__ == '__main__':
    cat01 = Cat('小白猫')
    cat01.eat()
    cat01.drink()
    cat01.shit()
    cat01.pee()
    cat01.cry()

    print("+"*20)
    dog01 = Dog("大黄狗")
    dog01.eat()
    dog01.drink()
    dog01.shit()
    dog01.pee()
    dog01.cry()