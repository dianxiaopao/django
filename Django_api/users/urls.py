# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import UserListPaginator

urlpatterns = [
    url(r'userListPaginator/$', UserListPaginator.as_view()),
]