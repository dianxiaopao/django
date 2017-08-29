# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from blog.models import Test,Contact,Tag


# Register your models here.
#将blog模块的 Test表交给 djnago admin 管理
#分开写
# admin.site.register(Test)
# admin.site.register(Contact)
# admin.site.register(Tag)
#集合写入
#admin.site.register([Test,Contact,Tag])

#详见 http://www.runoob.com/django/django-admin-manage-tool.html 

#我们可以自定义管理页面，来取代默认的页面。比如上面的 "add" 页面。我们想只显示 name 和 email 部分。
class ContactAdmin(admin.ModelAdmin):
    fields = ('name', 'email')


admin.site.register(Contact, ContactAdmin)
admin.site.register([Test, Tag])

