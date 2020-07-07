# 抽象类加抽象方法就等于面向对象编程中的接口
from abc import ABCMeta, abstractmethod

from study2020.study2020.class_study.class01 import Person


class interface(object,metaclass=ABCMeta):
    # __metaclass__ = ABCMeta  指定这是一个抽象类

    @abstractmethod  # 抽象方法
    def Lee(self):
        pass

                     # 没有 @abstractmethod  语法糖的不是抽象方法，子类可以不实现这个方法
    def Marlon(self):
        pass


class RelalizeInterfaceLee(interface):  # 必须实现interface中的所有函数，否则会编译错误
    def __init__(self):
        print('这是接口interface的实现')

    def Lee(self):
        print('实现Lee功能')

    # def Marlon(self):
    #     pass


class RelalizeInterfaceMarlon(interface):  # 必须实现interface中的所有函数，否则会编译错误
    def __init__(self):
        print('这是接口interface的实现')

    def Lee(self):
        pass

    def Marlon(self):
        print("实现Marlon功能")


if __name__ == '__main__':
    relalizeInterfaceLee = RelalizeInterfaceLee()
    relalizeInterfaceLee.Lee()
    relalizeInterfaceLee.Marlon()

    relalizeInterfaceMarlon = RelalizeInterfaceMarlon()
    relalizeInterfaceMarlon.Lee()
    relalizeInterfaceMarlon.Marlon()