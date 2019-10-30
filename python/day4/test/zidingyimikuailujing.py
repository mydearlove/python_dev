#author wangzhaoyang
import   os ,sys

print(sys.path)
x=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(x)
print(sys.path)
import  regress_test
import logging
logging.warning("user [alex] attempted wrong password more than 3 times")
logging.critical("server is down")