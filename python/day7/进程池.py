#author wangzhaoyang
import   multiprocessing
import   time
import   random
import   os

def  test1(msg):
    t_start = time.ctime()
    print("%s开始执行，进程号为%d"%(msg,os.getpid()))
    time.sleep(5)
    t_stop=time.time()
    print("%s执行完成，耗时%.2f" % (msg, t_stop-t_start))

if __name__ == '__main__':
    po=multiprocessing.Pool(3)
    for i in range(10):
        po.apply_async(test1,(i,))
    print("----start----")
    po.close()
    po.join()
    print("----end----")