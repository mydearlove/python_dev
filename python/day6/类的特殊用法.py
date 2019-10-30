#author wangzhaoyang
# class Foo:
#     """ 描述类信息，这是用于看片的神奇 """
#
#     def func(self):
#         pass
#
# obj=Foo()
# print(Foo.__doc__)
# print(obj.__module__)
# print(obj.__class__)
class Foo:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print('__call__')


obj = Foo()  # 执行 __init__
obj()  # 执行 __call__