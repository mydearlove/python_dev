#author wangzhaoyang
'''
name  = "wangzhaoyang"
name2 = name
print("my name is",name,name2
'''
name = input("Name:")
age = int(input("Age"))
print(type(age))
info = '''
------info of %s ------
Name:%s
Age:%d
''' %(name,name,age)
print(info)
info2 = '''
------info2 of  _name
Name:{_name}
Age:{_age}
'''.format(_name = name,
           _age = age)
info3 = '''
------info3 of {0}
Name:{0}
Age:{1}
'''.format(name,age)
print(info2)
print(info3)
