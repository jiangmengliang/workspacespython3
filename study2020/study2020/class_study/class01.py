# 创建类
class Person:
    #被称为构造函数，根据类创建对象时自动执行
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_name(self):
        print("姓名：",self.name)
    def get_age(self):
        print("年纪：",self.age)


#根据类class01创建对象
person01 = Person('jiang',27)
print(person01.name)
print(person01.age)
person01.get_name()
person01.get_age()