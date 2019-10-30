from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def  login(request):
    if  request.method ==  'GET':
        return   render(request,'login.html')
    elif request.method =="POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if  user =="root" and pwd =="123":
            #生成随机字符串
            #写到用户浏览器cookie
            #保存到session中
            #在随机字符串中对应的字典中设置相关内容
            request.session['username'] = user
            request.session['is_login'] = True
            return  redirect("/index")
        else:
            return render(request,'login.html')


def index(request):
    if  request.session.get('is_login',None):
        return   render(request,'index.html')
    else:
        return   HttpResponse("gun")
def logout(request):
    request.session.clear()
    return redirect('/login')