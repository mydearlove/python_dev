#author wangzhaoyang
import   threading
import   time
def sayhi(num):
    print("running on number:%s"%num)
    time.sleep(3)
if  __name__== '__main__':
    t1=threading.Thread(target=sayhi,args=(1,))
    t2=threading.Thread(target=sayhi,args=(2,))
    t3=threading.Thread(target=sayhi,args=(3,))
    t1.start()
    t2.start()
    t3.start()
    print(t1.getName())
    print(t2.getName())
    print(t3.getName())