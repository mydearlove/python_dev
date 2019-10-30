#author wangzhaoyang
import    paramiko,os
print(os.getcwd())
transport = paramiko.Transport(('VM_0_15_centos',22))
transport.connect(username='root',password='Gauss_234')
sftp = paramiko.SFTPClient.from_transport(transport)
#将本地文件上传至服务器
sftp.put('paramiko_test.py','/mnt/windows.test')
#将远程文件下载到本地
#sftp.get('remove_path','local_path')
transport.close()

