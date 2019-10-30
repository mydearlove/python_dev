#author wangzhaoyang
import   sqlalchemy
from sqlalchemy import   create_engine
from   sqlalchemy.ext.declarative import   declarative_base
from    sqlalchemy import   Column,Integer,String
from   sqlalchemy.orm  import   sessionmaker
##连接
engine=create_engine("mysql+pymysql://root:Gauss_234@139.155.131.188/dailyfresh",encoding='utf-8',echo=True)
#生成orm基类
base=declarative_base()
class user(base):
    __tablename__='wangzhaoyang'  #biaoming
    id= Column(Integer,primary_key=True)
    name=Column(String(32))
    password=Column(String(64))
#base.metadata.create_all(engine)
Session_class=sessionmaker(bind=engine)
Session=Session_class()
##插入数据
# user_obj = user(name="rr",password="123456")
# Session.add(user_obj)
# Session.commit()
##查询
#my_user=Session.query(user).filter_by(name="rr").first()
##修改
#my_user.name='uu'
#回滚
my_user = Session.query(user).filter_by(name="rr").first()
my_user.name="wwwww"
obj=user(name="wang",password="123456")
Session.add(obj)
print(Session.query(user.name,user.id,user.password).all())
Session.rollback()
print(Session.query(user.name,user.id,user.password).all())
#获取所有数据
#print(Session.query(user.name,user.id,user.password).all())

# my_user.name="gg"
# user_obj = user(name="kk",password="99999")
# Session.add(user_obj)
# print(my_user.id,my_user.name,my_user.password  )
