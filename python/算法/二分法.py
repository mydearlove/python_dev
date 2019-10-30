#author wangzhaoyang
import   random
def   bin_search(data_set,value):
    low = 0
    high= len(data_set)
    while low <= high:
        mid = (low+high)//2
        if data_set[mid] == value:
            return  mid
        elif data_set[mid] < value:
            low = mid +1
        else:
            high =mid-1
data = list(range(1000))

result = []
def random_list(n):

    ids = list(range(1000,1000+n))
    a1 = ['zhang','wang','li','zhao']
    a2 = ['tian','xia','tai','ping']
    a3 = ['guo','jun','']
    for i  in  range(n):
        age = random.randint(18,40)
        id = ids[i]
        name = random.choice(a1)+random.choice(a2)+random.choice(a3)
        dict= {'ID':id,'NAME':name,'AGE':age}
        result.append(dict)
    print(result)

random_list(10)
for name  in  result:
    print(name)

[1,3,5,2,3,6,7,8]

7