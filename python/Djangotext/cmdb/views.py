from django.shortcuts import render
from    django.shortcuts import HttpResponse
from   django.shortcuts import  redirect
# def home(request):
#     return  HttpResponse("<h1>cmdb<h1>")
def login(request):
    #return  render(request,"login.html")
    error_msg=""
    if request.method == "POST":
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        if user == "root"  and pwd == "123":
            return   redirect('/home')
        else:
            error_msg = "用户名或者密码错误"
    return render(request,'login.html',{'error_msg':error_msg})
USER_LIST = [
    {'id': 1, 'username': 'alex', 'email': 'asdfasdf', "gender": '男'},
    {'id': 2, 'username': 'eriuc', 'email': 'asdfasdf', "gender": '男'},
    {"id": 3,'username': 'seven', 'email': 'asdfasdf', "gender": '男'},
]
USER_DICT = {
    '1': {'name': 'root1', 'email': 'root@live.com'},
    '2': {'name': 'root2', 'email': 'root@live.com'},
    '3': {'name': 'root3', 'email': 'root@live.com'},
    '4': {'name': 'root4', 'email': 'root@live.com'},
    '5': {'name': 'root5', 'email': 'root@live.com'},
}

def  index(request):
    return render(request,'index.html',{'user_dict':USER_DICT})

# def detail(request):
#     nid = request.GET.get('nid')
#     detail_info = USER_DICT[nid]
#     return render(request,'detail.html',{'detail_info':detail_info})
def detail(request,nid):
    detail_info = USER_DICT[nid]
    return render(request,'detail.html',{'detail_info':detail_info})




def  home(request):
    if request.method =="POST":
        u = request.POST.get('username')
        e = request.POST.get('email')
        g = request.POST.get('gender')
        temp = {'username': u, 'email': e, "gender": g}
        print(temp)
        USER_LIST.append(temp)
    return render(request, "home.html",{'user_list':USER_LIST})


