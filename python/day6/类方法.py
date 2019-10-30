#author wangzhaoyang
class Dog(object):
    name="wang"
    def __init__(self, name):
        self.name = name

    @classmethod
    def eat(self):
        print("%s is eating" %self.name)


d = Dog("ChenRonghua")
d.eat()