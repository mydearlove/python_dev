#author wangzhaoyang
import   time
# def test():
#     pass
#     return 0
# def   test(x,y=4):
#     print(x,y)
# #y=test(1,y=2)
# def test1(*args):
#     print(args)
# test1(1,2,3,4,5)
# test1(*[1,2,3,4,5,6])
# def test(x,y):
#     res = x*y
#     return   res
# c= test(1,2)
# print(c)
def student_register(name,age,country,course):
    print("------注册学生信息------")
    print("name:",name)
    print("age",age)
    print("country",country)
    print("course",course)
student_register("ligang",22,"CN","python_devops")
student_register("zhangyang",23,"CN","java")
student_register("zhangqiang",27,"CN","linux")