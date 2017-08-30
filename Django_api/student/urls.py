# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import StudentList, StudentDetail,StudentListPaginator

urlpatterns = [
    url(r'students/$', StudentList.as_view()),
    url(r'studentListPaginator/*$', StudentListPaginator.as_view()), #分页查询
    # “(?P<name>...) 子串匹配到的内容将可以用命名的name来提取url中的值。组的name必须是有效的python标识符，而且在本表达式内不重名。”
    url(r'studentdetail/(?P<name>.+)/$', StudentDetail.as_view()),

    url(r'studentdetail/$', StudentDetail.as_view()),
]