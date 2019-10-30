#author wangzhaoyang

class   BaseResponse(object):
    def  __init__(self):
        self.status = False
        self.name=""
        self.data = None
response = BaseResponse()
response.status=True
print(response.__dict__)