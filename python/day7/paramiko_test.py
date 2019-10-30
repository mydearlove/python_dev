#author wangzhaoyang
import  paramiko
#创建SSH对象
ssh = paramiko.SSHClient()
#y允许连接不在know_hosts文件里面的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接服务器
ssh.connect(hostname='VM_0_15_centos',port=22,username='root',password='Gauss_234')
stdin,stdout,stderr = ssh.exec_command('')
result = stdout.read()
print(result)
ssh.close()