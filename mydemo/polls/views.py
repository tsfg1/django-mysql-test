from django.shortcuts import render
from django.http.response import HttpResponse
from polls.models import StudentInfo
import random



# Create your views here.

def toLogin_view(request):
    return render(request, 'login.html')

def Login_view(request):
    u = request.POST.get("user_1")
    p = request.POST.get("pwd_1")

    if u and p:
        c = StudentInfo.objects.filter(stu_name=u, stu_psw=p).count()
        if c>=1:
            return HttpResponse("登陆成功")
        else:
            return HttpResponse("账号密码错误")    
    else:
        return HttpResponse("请输入正确的账号和密码")

def toregister_view(request):
    return render(request, 'register.html')        

def register_view(request):
    u = request.POST.get("user_2")
    p = request.POST.get("pwd_2")

    if u and p:
        stu = StudentInfo(stu_id=str(random.randrange(1111,9999)),stu_name=u, stu_psw=p)
        stu.save()
        return HttpResponse("注册成功")
    else:
        return HttpResponse("请输入完整的账号和密码")

