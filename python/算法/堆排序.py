#author wangzhaoyang
from  collections import   deque
#####python  neizhi fangfa
import heapq
import  random
heap = []
data = list(range(10000))
random.shuffle(data)
# for  num in data:
#     heapq.heappush(heap,num)
# for i in range(len(heap)):
#     print(heapq.heappop(heap))
print(heapq.nsmallest(10,data))
print(heapq.nlargest(10,data))