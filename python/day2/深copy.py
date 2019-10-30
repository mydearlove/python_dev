#author wangzhaoyang
from   copy  import   deepcopy
li=[1,2,3,4,[1,2,3,4]]
li1=li
li2=deepcopy(li)
li[4][0]=10
print(li1)
print(li2)