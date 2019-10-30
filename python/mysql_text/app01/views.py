from django.shortcuts import render
from   django.shortcuts import   HttpResponse
from   django.shortcuts import   redirect
from   app01  import    models
# Create your views here.

def orm(request):
    ##增
    # models.UserInfo.objects.create(
    #     username = 'root',
    #     password = '123'
    # )
    #查
    # result = models.UserInfo.objects.all()
    # result = models.UserInfo.objects.filter(username='root')
    # for row in result:
    #     print(row.id,row.username,row.password)
    # print(result)
    models.UserInfo.objects.filter(id=3).update(password="69")
    return   HttpResponse('orm')
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method =='POST':
        u = request.POST.get('user')
        p=request.POST.get('pwd')
        obj= models.UserInfo.objects.filter(username=u,password=p)
        if obj:
            return  redirect('/cmdb/index/')
        else:
            return   render(request,'login.html')
    else:
        return   redirect('/index/')

def index(request):
    return   render(request,'index.html')

def  user_info(request):
    if request.method == "GET":
        user_list = models.UserInfo.objects.all()
        return   render(request,'user_info.html',{'user_list':user_list})
    elif request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        models.UserInfo.objects.create(username=u, password=p)
        return redirect('/cmdb/user_info/')

def  user_detail(request,nid):
    obj=models.UserInfo.objects.filter(id=nid).first()
    #如果不存在直接报错
    #models.UserInfo.objects.get(id=nid)
    return   render(request,'user_detail.html',{'obj':obj})

def   userdel(request,nid):
    print(nid)
    models.UserInfo.objects.filter(id=nid).delete()
    return  redirect("/cmdb/user_info/")