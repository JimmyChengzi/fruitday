from django.shortcuts import render
from .models import *
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.

def register_(request):
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method == 'POST':
        #创建用户信息表对象
        new_user = UserInfo()
        #username从前端取,如果没有就为空
        new_user.uname = request.POST.get('username','')
        a = UserInfo.objects.filter(uname=new_user.uname)
        #条件成立都不能注册
        if len(a) > 0:
            return render(request,'register.html',{'msg':'用户名存在'})
        if request.POST.get('pwd') != request.POST.get('cpwd'):
            return render(request,'register.html',{'msg':'两次密码不一致'})
        #条件不成表示用户名没被注册且两次密码一致
        #make_password 加密再存储到数据库
        new_user.upwd = make_password(request.POST.get('pwd'),None,'pbkdf2_sha1')
        #登录用到的,明文是pwd,密文是pbkdf2_sha1
        # T/F = check_password(明文,密文)
        new_user.uemail = request.POST.get('uemail')
        new_user.uphone = request.POST.get('uphone')
        new_user.save()
        return


