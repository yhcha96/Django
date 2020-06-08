"""intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages import views # from (app이름) import (파일이름)

urlpatterns = [
    path('admin/', admin.site.urls),
    # 안녕하세요
    # 점심
    path('index/', views.index), # path(경로, 함수)
    # 안녕하세요, <이름>
    path('hello/<name>/', views.hello), # <name> : <변수명>
    # 두 수 곱
    # path('multiply/<num1>/<num2>/', views.multiply)
    path('multiply/<int:num1>/<int:num2>/', views.multiply), # 기본 <str:num1> 띄어쓰기 불가능
    # django template language
    path('dtl/',views.dtl),
    # Is it your Birthday
    path('isUrBRD/', views.isUrBRD),
]
