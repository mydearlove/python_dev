#author wangzhaoyang
f = open("test","r",encoding=("utf-8"))
f_new=open("test1","w",encoding=("utf-8"))
for line in f:
    if "毁灭性的的那种"  in line:
        line=line.replace("毁灭性的的那种","wangzhaoyang123")
    f_new.write(line)
f.close()
f_new.close()
