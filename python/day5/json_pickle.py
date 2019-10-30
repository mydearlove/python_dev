#author wangzhaoyang
import   json
data = {"k1":123,"k2":234}
f= open("test.text","w")
f.write(json.dumps(data))
