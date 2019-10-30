#author wangzhaoyang
import time
def auth(auth_type):
    print(auth_type)
    def out_warper(func):
        def warper(*args,**kwargs):
            start_time=time.time()
            print(func(*args))
            #print(func(*args))
            return
        return   warper
    return  out_warper
@auth(auth_type="local")
def run(*args,**kwargs):
    print("我要开始休息了")
    print(args[1])
    time.sleep(1)
    return  1
run(1,2,3)