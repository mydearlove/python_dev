#author wangzhaoyang
import time
print(time.clock())
print(time.altzone)
print(time.asctime())
print(time.localtime())
print(time.gmtime(time.time()-800000))
print(time.asctime(time.localtime()))
print(time.ctime())
string_2_struct = time.strptime("2016/05/22","%Y/%m/%d")
print(string_2_struct)
struct_2_stamp = time.mktime(string_2_struct)
print(struct_2_stamp)
print(time.gmtime(time.time()-86640))
print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()) )
