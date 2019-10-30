#author wangzhaoyang
# ao=dict(zip(('a','b','c'),(1,2,3)))
# A3=[ao[s] for s in ao]
# print(A3)
# for i in  ao:
#     print(ao[i])
# info = {
#     'stu1101': "TengLan Wu",
#     'stu1102': "LongZe Luola",
#     'stu1103': "XiaoZe Maliya",
# }
# for  i   in  info:
#     print(i)
# l=[]
# for i in xrange(5):
#      print(i)
# print("******")
# l=[1,2,3]
# try:
#     a=l[4]
# except IndexError as e:
#     print(e)
# try:
#     s=None
#     if s is  None:
#         print("***")
#         raise  NameError
#     print(len(s))
# except TypeError:
#     print("#####")
# import   sys
# #print(sys.platform,"#",sys.version)
# try:
#     sys.exit(1)
# except SystemExit as e:
#     print(e)
# d={i:i*i for i in range(10)}
# print(d)
#print('ssdsdsd'[::-1])
# import  re
# str1="k:1|k1:2|k2:3"
# str2=str1.split("|")
# dict={}
# for raw in str2:
#     #li=(raw.split(":"))
#     #key,value=raw.split(":")
#     print(raw.split(':'))
#     #print(key,value)
#     #dict[key]=value
# print(dict)
# alist=[{'name':'a','age':20},{'name':'b','age':21},{'name':'b','age':22}]
# def sort_by_age(list1):
#     return  sorted(alist,key=lambda x:x['age'],reverse=True)
# print(sort_by_age(alist))
# list=[1,2,3,4,5,6,7,1,2,3,4,5]
# set1=set(list)
# print(set1)
# a=[1,2,3,4]
# b=[3,4,5,6]
# A=set(a)
# B=set(b)
# overlap=A^B
# diff=A&B
# print(overlap)
# print(diff)
# li= [i for i in range(10)]
# print(li[1:])
# print(li[1:7])
# print(li[3:7])
# print(li[9])
# print(li[1:10:2])
# import   random
# import   cProfile
# def f1(lIn):
#     l1 = sorted(lIn)
#     l2 = [i for i in l1 if i<5]
#     return [i*i for i in l2]
# li=[i for i in  range(1000)]
# cProfile.run('f1(li)')
#
# print(f1(li))
# alist=[]
# def div(li):
#     for num in li:
#         print("***")
#         if num%6==0:
#             print("****")
#             print(num)
#             alist.append(num)
#
# li=[i for i in  range(1,101)]
# div(li)
# print(alist)
#
# a=map(lambda x:x+1,range(10))
# print(list(a))
#reduce(lambda x,y:x*y ,range(2))
# a=filter(lambda x:x%2,range(10))
# print(list(a))
# print(dir('a'))
# def mul():
#     return [lambda x, i=i:i*x for i in range(4)]
# print(mul())

# x=(i for i in range(10))
# print(type(x))
#0 1 1 2 3 5 8
# def fib(index):
#     fibs=[0,1]
#     while len(fibs)<10:
#         fibs.append(fibs[-2]+fibs[-1])
#     print(fibs)
#     return   fibs
# fib(10)
# # fibs=[0,1]
# for i in range(8):
#     fibs.append(fibs[-2]+fibs[-1])
# print(fibs)
# def fib(n):
#     a,b=0,1
#     while a<10:
#         print(a)
#         a,b=b,a+b
# fib(10)
# def fib(n):
#     if n==0 or n==1:
#         return  1
#     else:
#         return fib(n-1)+fib(n-2)
# for i in range(10):
#     print(fib(i))
# str="{1}{0}"
# str1=str.format("hello","python")
# print(str1)
# a=('1','2')
# del a[0]
# from   functools   import    reduce
# sum=reduce(lambda x,y:x*y,range(1,101))
# print(sum)
x=y=z=1
x+=y