#author wangzhaoyang
import   random
def count_sort(li,max_num):
    count = [ 0 for  i in  range(max_num+1)]
    for num in li:
        count[num] +=1
    i=0
    for  num,m in  enumerate(count):
        for  j in  range(m):  #将重复的数打印m次
            li[i] = num
            i +=1
data = []
for i in  range(100):
    data.append(random.randint(0,100))
print(data)
count_sort(data,100)
print(data)