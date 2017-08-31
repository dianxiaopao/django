# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import  SclassList

urlpatterns = [
    url(r'sclassList/$', SclassList.as_view()),
]