import  getpass
_username = 'wangzhaoyang'
_password = 'test123'
username = input("username:")
password = input("password")
if ( username == _username and  password == _password):
    print("welcome user {name}".format(name = username))
else:
    print("Invalid username or password")

