from django.shortcuts import render,HttpResponse,redirect
from  app01  import models
# Create your views here.
def  login(request):
    return   HttpResponse("ok")
def article(request,*args,**kwargs):
    condition={}
    for k,v in kwargs.items():
        kwargs[k]=int(v)
        if  v=='0':
            pass
        else:
            condition[k]=v
    article_type_list = models.ArticleType.objects.all()
    category_list = models.Category.objects.all()
    result=models.Article.objects.filter(**condition)
    print(kwargs)
    return   render(request,
                    'article.html',
                    {"result":result,
                     "article_type_list":article_type_list,
                     "category_list":category_list,
                     "arg_dict":kwargs,
                     })
