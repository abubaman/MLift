from django.urls import path
from django.contrib import admin
from . import views

app_name = 'accounts'

urlpatterns = [
    path('userinfo/', views.userinfo, name='userinfo'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.log_out, name='logout'),
    path('update/', views.update, name='update'),
    path('mypage/', views.mypage, name='mypage'),
    path('formtest/', views.formtest, name='formtest'),
    path('api/user/', views.userInfoAPI, name='userinfoapi'),
    path('api/user/<str:username>', views.userUpdateAPI, name='userupdateapi'),
]
