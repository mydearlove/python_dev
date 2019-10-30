#author wangzhaoyang
import  socket
import   sqlalchemy
client = socket.socket()  #声明socket类型，及生成socket连接对象
client.connect(('localhost',9999))
while  True:
    msg = input(">>:").strip()
    if  len(msg) == 0 :  continue
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print("recv:",data.decode())
client