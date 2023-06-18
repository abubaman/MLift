from django.shortcuts import render, redirect, reverse

from django.contrib import auth
from .models import User

from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from . import forms

from django.views import View

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view

from django.http import Http404


import qrcode
import os


# Create your views here.
def formtest(request):
    return render(request, 'formtest.html')

def userinfo(request):
    if request.user.is_authenticated:
        context = {
                'username' : request.user.username,
                'clg_start' : request.user.clg_start,
                'clg_end' : request.user.clg_end,
                'clg_type' : request.user.clg_type,
                'clg_type_text' : request.user.get_clg_type_display,
                'clg_iter' : request.user.clg_iter,
                'clg_iter_text' : request.user.get_clg_iter_display,
                'noti_bool' : request.user.noti_bool,
                'noti_bool_text' : request.user.get_noti_bool_display,
                'noti_time' : request.user.noti_time,
                'noti_time_text' : request.user.get_noti_time_display,
                'user_gender' : request.user.user_gender,
                'user_gender_text' : request.user.get_user_gender_display,
                'user_height' : request.user.user_height,
                'user_weight' : request.user.user_weight,
        }
        return render(request, 'userinfo.html', context)

    else:
        context = {
                'login' : "Not logged in"
        }
        return redirect('accounts:login')

def update(request):
    if request.method=='POST':
        form = forms.CustomUserChangeForm(request.POST, instance = request.user)
      
        if form.is_valid():
            form.save()
            context = {
                'username' : request.user.username,
                'clg_start' : request.user.clg_start,
                'clg_end' : request.user.clg_end,
                'clg_type' : request.user.clg_type,
                'clg_type_text' : request.user.get_clg_type_display,
                'clg_iter' : request.user.clg_iter,
                'noti_bool' : request.user.noti_bool,
                'noti_time' : request.user.noti_time,
                'user_gender' : request.user.user_gender,
                'user_height' : request.user.user_height,
                'user_weight' : request.user.user_weight,
            }
            #print(context)
            #print(request)
            return redirect(reverse("accounts:userinfo"))
        else:
            print('not valid')
            #messages.success(request, 'Userinfo was modified successfully.')
           
    else:
        form = forms.CustomUserChangeForm(instance = request.user)
        context ={
                'form':form,
                'username': request.user.username,
                #'grc_pass' : request.user.grc_pass
        }
        return render(request, 'update.html',context)
    #form.grc_telegram(initial=request.user.grc_telegram)
    #context={
    #        'form':form,
    #        'username' : request.user.username
    #}
    #return render(request, 'update.html', context)



class SignUpView(FormView):
    template_name = "signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("accounts:userinfo")
    

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        
        # for qr code
        img = qrcode.make(username)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filename = username & ".png"
        url = os.path.join(BASE_DIR, 'static', 'qrcode', filename)
        img.save("url")

        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)



class LoginView(View):
    # def get(self, request):
    #     form = forms.LoginForm()
    #     context = {"form": form}
    #     return render(request, "login.html", context)
    #
    # def post(self, request):
    #     form = forms.LoginForm(request.Post)
    #     if form.is_valie():
    #         print(form.cleaned_data)
    #     context = {"form":form}
    #     return render(request, "login.html", context)
    def get(self,request):
        form = forms.LoginForm()
        context = {"form":form}
        return render(request, "login.html", context)

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(reverse("accounts:mypage"))
        context = {"form":form}
        return render(request, "login.html", context)

#def login1(request):
#    return render(request,"login1.html")

def log_out(request):
    logout(request)
    return redirect(reverse("accounts:login"))


def mypage(request):
    if request.user.is_authenticated:
        context = {
                'username' : request.user.username,
                'clg_start' : request.user.clg_start,
                'clg_end' : request.user.clg_end,
                'clg_type' : request.user.clg_type,
                'clg_type_text' : request.user.get_clg_type_display,
                'clg_iter' : request.user.clg_iter,
                'clg_iter_text' : request.user.get_clg_iter_display,
                'noti_bool' : request.user.noti_bool,
                'noti_bool_text' : request.user.get_noti_bool_display,
                'noti_time' : request.user.noti_time,
                'noti_time_text' : request.user.get_noti_time_display,
                'user_gender' : request.user.user_gender,
                'user_gender_text' : request.user.get_user_gender_display,
                'user_height' : request.user.user_height,
                'user_weight' : request.user.user_weight,
                'calorie' : request.user.calorie,
                'get_point' : request.user.get_point,
                'accum_point' : request.user.accum_point,
        }
        return render(request, 'mypage.html', context)

    else:
        context = {
                'login' : "Not logged in"
        }
        return redirect('accounts:login')




@api_view(['GET','PUT']) #GET, PUT 모두 가능하도록 함. username을 않넣고 다른 값만 업데이트하려면 serializer에서 username FALSE해줘야함.
def userUpdateAPI(request, username):
    if request.method == 'GET':
        queryset = User.objects.all()
        print(queryset)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    if request.method == 'PUT':
        model = User.objects.get(username = username)
        serializer = UserSerializer(model, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET']) #전체 리스트는 GET만 가능하도록 함.
def userInfoAPI(request):
    if request.method == 'GET':
        queryset = User.objects.all()
        print(queryset)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)