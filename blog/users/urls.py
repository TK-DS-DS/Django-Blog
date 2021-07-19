#进行users 子应用的视图路由
from django.urls import path
from users.views import RegisterView
urlpatterns=[
    #path的第一个参数
    path('register/',RegisterView.as_view(),name='register'),
]