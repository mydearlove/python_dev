#author wangzhaoyang
# L = [1,2,3,4,5,6]
# L[index] += 1
# # print(L)
# b = [i + 1 for i in range(10)]
# print(b)
# a = (i + 1 for i in range(10))
# # print(a)
# # for i in a:
# #    print(i)
# for  index,i in enumerate(L):
def fib(max):
    n,a,b = 0 ,0 ,1
    while n < max:
        print(b)
        a,b = b,a+b
        n += 1
    return  'done'
fib(10)

