#author wangzhaoyang
import   time
user,passwd = "wangzhaoyang","123456"
def auth(auth_type):
    print(auth_type)
    def out_warper(func):
        def warper(*args, **kwargs):
            if auth_type == "local":
                username = input("username>>").strip()
                password = input("password>>").strip()
                if user == username and passwd == password:
                    print("\033[32;1m User has passwd authentication\033[0m")
                    res = func(*args, **kwargs)
                    print("after authentication")
                    return res
                else:
                    exit("\033[31;1m Invalid username  or  password\033[0m")
            elif auth_type == "ldap":
                print("我还没有做ldap")

        return warper
    return out_warper
#@auth # index = warp  将warp的内存地址赋给index函数，index（）就相当于warp（），
def index():
    print("welcome to index page")
    return   "from   index"
@auth(auth_type = 'local')
def home():
    print("welcome to home  page")
    return    "from   home"
@auth(auth_type = 'ldap')
def bbs():
    print("welcome  to nns page")
home()
print(index())
bbs()
