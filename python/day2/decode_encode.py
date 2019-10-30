#author wangzhaoyang
import   sys
print(sys.getdefaultencoding())
msg = "我爱北京天安门"
msg_gb2312= msg.encode('gb2312')
print(msg_gb2312)
gb2312_to_unicode = msg_gb2312.decode('gb2312')
print(gb2312_to_unicode)
gb2312_to_utf8 = msg_gb2312.decode('gb2312').encode('utf-8')
print(gb2312_to_utf8)