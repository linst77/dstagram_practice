from django.urls import path
from django.contrib.auth import views as auth_view
from .views import *

# profile은 login시 django가 자동으로 연결해 준다.
# 1. profile 만들기
# 2. profile 페이지가 아닌 다른 페이지로 보내기 (a, 장고 설정변경, b,: 웹서버에서 redirect)
# config/settings 파일에 LOGIN_REDIRECT_URL = '/' 를 추가한다

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='registration/logout.html'), name="logout"),
    path('register/', register, name="register"),

]
