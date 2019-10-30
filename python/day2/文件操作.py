#author wangzhaoyang
# f=open('test1','r',encoding=('utf8'))
# for  line in f:
#     print(line)
with  open('test1','r+',encoding=('utf8'))  as f:
    f.write('this is  test')
    for  line  in  f:
        print(line)

