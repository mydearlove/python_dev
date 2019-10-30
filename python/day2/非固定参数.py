#author wangzhaoyang
def test(*args):
    print(args)
test(1,2,3,4,'test','name','[1,2,3]')
def test(**kwargs):
    print(kwargs)
#test(name = 'liyang',age= 25,course = 'python')
