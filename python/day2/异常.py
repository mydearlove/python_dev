#author wangzhaoyang
try:
    li=[1,2,3,4]
    li[3]
except IndexError  as e:
    print(e)
else:
    print('meiyouyichang')
finally:
    print('end')