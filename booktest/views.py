from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

#
def index(request):
    # 传递用户登录状态信息给模板
    context = {
        'title': '知阅 - 在线阅读平台',
        'user': request.user,
        'is_authenticated': request.user.is_authenticated
    }
    return render(request,'booktest/index.html',context)
def zhouchengyi(request):
    return HttpResponse("230207977周承屹")

# 阅读网站主页视图
def reader_home(request):
    # 可以在这里添加需要传递给模板的上下文数据
    context = {
        'title': '知阅 - 在线阅读平台',
        'user': request.user  # 传递当前登录用户信息
    }
    return render(request, 'booktest/reader_home.html', context)

def login(request):
    if request.method == 'POST':
        # 获取表单数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # 验证用户
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # 登录用户
            auth_login(request, user)
            # 登录成功后重定向到主页
            return redirect('/')
        else:
            # 登录失败，显示错误信息
            return render(request, 'booktest/login.html', {'error_message': '用户名或密码错误'})
    
    # GET请求，显示登录页面
    return render(request, 'booktest/login.html')

def register(request):
    if request.method == 'POST':
        # 获取表单数据
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # 表单验证
        if not email or not password1 or not password2:
            return render(request, 'booktest/register.html', {'error_message': '请填写所有必填字段'})
            
        if password1 != password2:
            return render(request, 'booktest/register.html', {'error_message': '两次输入的密码不一致'})
            
        # 检查邮箱是否已被注册
        if User.objects.filter(email=email).exists():
            return render(request, 'booktest/register.html', {'error_message': '该邮箱已被注册'})
            
        # 创建用户，使用邮箱作为用户名
        try:
            user = User.objects.create_user(username=email, email=email, password=password1)
            user.save()
            
            # 注册成功后自动登录用户
            auth_login(request, user)
            
            # 重定向到主页
            return redirect('/')
        except Exception as e:
            return render(request, 'booktest/register.html', {'error_message': f'注册失败：{str(e)}'})
    
    # GET请求，显示注册页面
    return render(request, 'booktest/register.html')
