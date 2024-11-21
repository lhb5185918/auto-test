from django.urls import path

from web.views.account import LoginView

from web.views.account import RegisterView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),  # test路径 对应views中的test函数
    path("register/", RegisterView.as_view(), name="register"),
]
