from django.shortcuts import render,HttpResponse,redirect
from  app01   import  models
# Create your views here.
def  business(request):
    v1 =  models.Business.objects.all()
    #quertset
    # [obj(id,caption,code),obj(id,caption,code),obj(id,caption,code) ]
    v2 = models.Business.objects.all().values("id",'caption')
    # QuerySet
    # [{'id':1,'caption': '��ά��'},{'id':1,'caption': '��ά��'},...]

    v3 = models.Business.objects.all().values_list("id","caption")
    # QuerySet
    # [(1,yunwei),(2,kaifa)]
    return   render(request,"business.html",{'v1':v1,"v2":v2,"v3":v3})

def  host(request):
    v1 = models.Host.objects.all()
    print(v1)
    return   HttpResponse("ok")