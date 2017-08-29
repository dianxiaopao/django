"""Django_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from student.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'students/$', StudentList.as_view()),
    # “(?P<name>...) 子串匹配到的内容将可以用命名的name来提取url中的值。组的name必须是有效的python标识符，而且在本表达式内不重名。”
    url(r'students/(?P<name>[a-zA-Z]+)/$', StudentDetail.as_view()),
]
