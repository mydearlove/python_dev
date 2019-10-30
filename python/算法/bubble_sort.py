#author wangzhaoyang
import    random
def  bubble_sort(li):

    for  i   in range(len(li)-1):
        exchange = False
        for  j in range(len(li)-i-1):
             if li[j] >  li[j+1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange =  True
        if not  exchange:
            break
data = [1,2,3,4,6,5]
#random.shuffle(data)
bubble_sort(data)
print(data)