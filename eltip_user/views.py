# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from eltip_user.models import User, Account
@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            user_data = User.objects.get(account=username, password=password)
            if user_data:
                messages.success(request, '歡迎回來！')
                # 儲存登入狀態session
                request.session['login_id'] = user_data.id
                return redirect('eltip_user.views.index')
           
        except Exception, ex:
            messages.error(request, ex.message)
            #messages.error(request, '帳號或密碼錯誤！')
            return render(request, 'login.html')
    return render_to_response('login.html')

@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            name = request.POST['name']
            company = request.POST['company']
            position = request.POST['position']
            bank = request.POST['bank']
            user_data = User.objects.create(
                account=username,
                email=email,
                password=password,
                name=name,
                company=company,
                position=position
            )
            user_account = Account.objects.create(
                uid = user_data.id,
                credit = bank
            )
            messages.success(request, '歡迎加入!')
            # 預設註冊完即登入，儲存session
            request.session['login_id'] = user_data.id
            return redirect('eltip_user.views.index')
        except Exception, ex:
            messages.error(request, '註冊發生錯誤！帳號或Email重複！')
            return render(request, 'register.html')
    return render_to_response('register.html')

@csrf_exempt
def index(request):
    isLogin = False
    userlist = []
    if 'logout' in request.GET:
        request.session['login_id'] = ''
        return redirect('eltip_user.views.index')
    if request.session['login_id']:
        isLogin = True
    if request.method == 'GET' and 'find' in request.GET:
        user_data = User.objects.filter(account__contains=request.GET['find'])
        user_data2 = User.objects.filter(name__contains=request.GET['find'])
        userid = set()
        for u in user_data:
            userid.add(u.account)
        for u in user_data2:
            userid.add(u.account)
        for u in userid:
            info = User.objects.get(account=u)
            userinfo = {}
            userinfo['account'] = info.account
            userinfo['name'] = info.name
            userlist.append(userinfo)
    return render(request, 'index.html', locals())

@csrf_exempt
def tip(request, username):
    name, company, position = '', '', ''
    try:
        user_data = User.objects.get(account=username)
        name, company, position = user_data.name, user_data.company, user_data.position
    except Exception, ex:
        messages.error(request, '找不到這個人:('+ ex.message)
        return redirect('eltip_user.views.index')
    return render(request, 'tip.html', locals())

@csrf_exempt
def profile(request):
    username, password, name, email, company, position, bank = '','','','','','',''
    if request.session['login_id']:
        user_data = User.objects.get(id=request.session['login_id'])
        username, password, name, email, company, position = \
            user_data.account, user_data.password, user_data.name, user_data.email, \
            user_data.company, user_data.position
        bank = Account.objects.get(uid=user_data.id).credit
    else:
        return redirect('eltip_user.views.index')
    return render(request, 'profile.html', locals())
