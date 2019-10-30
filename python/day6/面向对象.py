#author wangzhaoyang
# class  Foo(object):
#     def __init__(self,name,age):
#         self.name= name
#         self.age = age
#     def talk(self,lauguage):
#         print("%s talking %s" %(self.name,lauguage))
# F=Foo('ALEX',22)
# F.talk('English')
class People(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.friends = []
    def eat(self):
        print("%s is eating ..." %self.name)
    def talk(self):
        print("%s is talking..." %self.name)
    def sleep(self):
        print("%s is  sleeping..."%self.name)
class Relation(object):
    def make_friends(self,obj):
        print("%s makeing   friends  with %s " %(self.name,obj.name))
class  Man(People,Relation):
    def __init__(self,name,age,money):
        #People.__init__(self,name,age)
        super(Man,self) .__init__(name,age)
        self.money = money
        print("%s 一出生就有 %s是"%(self.name,self.money))
    def sleep(self):
        People.sleep(self)
        print("sleep 20s")
class Woman(People):
    def __init__(self,name,age):
        self.name = name
        self.age = age

M = Man('alex',22,100)
W = Woman('jack',23,)
M.make_friends(W)
M.sleep()
