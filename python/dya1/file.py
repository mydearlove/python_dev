#author wangzhaoyang
#f= open('test','r',encoding=('utf-8'))  #  r,w,a,r+.w+,a+
#f.read()
f= open('test1','a',encoding=('utf-8'))  #  r,w,a,r+.w+,a+（追加读）
f.write(" \nthis is test") #写
f.read( )
#first_line = f.readline()
# read 读全部
#print(first_line)
f.close()
f.readlines()#  liebiao,一次性全部读到内存中
f.readline()  #  一行一行的读，但是会把文件先读到到内存中

for line in f:  ###一行一行的读，效率最高，最常用的
    print(line)
print(f.tell())  ##打印指针位置
f.seek(0)   ##将文件指针移动到指定位置
print(f.encoding)  ##打印文件编码
print(f.name)  #打印文件，名字

f.flush()  #将文件刷新到硬盘上，强制刷到硬盘上
f.truncate(10)  #截断，截取十个字符