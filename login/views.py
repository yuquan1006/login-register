import json

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import Http404
from django.urls import reverse
from .models import User
# Create your views here.


def logincheck(func):
    def wrapper(request,*args, **kwargs):
        if not request.session.get('is_login'):
            return HttpResponseRedirect('/login/')
        return func(request, *args, **kwargs)
    return wrapper

# 密码加密
import hashlib
def hash_code(s,key='york'):
    h = hashlib.sha256()
    s+=key
    h.update(s.encode('utf-8'))
    print(h.hexdigest())
    return h.hexdigest()


@logincheck
def index(request):
    pass
    return render(request,"login/index.html")

def login(request):
    if request.session.get('is_login',None):
        # 禁止重复登录
        return HttpResponseRedirect('/index/')
    if request.method == 'POST':
        name = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(name__exact=name,passWord__exact=hash_code(password)).count()>0:
            print("登录成功")
            request.session['is_login'] = True
            request.session['user_name'] = name
            return HttpResponseRedirect('/index/')
        else:
            print("用户名或者密码错误！")
            return render(request,"login/login.html",context={"errorMsg":"用户名或者密码错误！"})
    else:
        return render(request,"login/login.html")



def register(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        email = request.POST.get('email')
        sex = request.POST.get('sex')
        if confirmpassword != password :
            errorMsg = "两次密码不重复"
            return render(request,"login/register.html",context={"errorMsg":errorMsg})
        if User.objects.filter(name__exact=username).count()>0:
            errorMsg = '用户名已注册，请更换后重新注册'
            return render(request,"login/register.html",context={"errorMsg":errorMsg})
        if User.objects.filter(email__exact=email).count()>0:
            errorMsg = '邮箱已注册，请更换后重新注册'
            return render(request,"login/register.html",context={"errorMsg":errorMsg})

        User.objects.create(name=username,passWord=hash_code(password),email=email,sex=sex)
        return HttpResponseRedirect('/login/')
    else:
        return render(request,"login/register.html")

@logincheck
def logout(request):
    if not request.session.get('is_login',None):
        return render(request,"login/login.html")
    request.session.flush() #  删除当前的会话数据和会话cookie。经常用在用户退出后，删除会话。
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_name']
    return render(request, "login/login.html")





# request.session
#    当session启用后，传递给视图request参数的HttpRequest对象将包含一个session属性，就像一个字典对象一样。你可以在Django的任何地方读写request.session属性，或者多次编辑使用它。