# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class UserGroup(models.Model):
    class Meta:
        db_table = 't_usergroup'
    uid = models.AutoField(primary_key=True)
    # unique=True（代表不能重名
    caption = models.CharField(max_length=32,unique=True)
    #自动创建，永远是创建时的时间
    ctime = models.DateField(auto_now_add=True)
    #自动创建----无论添加或者修改，都是当前操作时间
    uptime = models.DateField(auto_now=True)


class UserInfo(models.Model):
    # django admin显示字段中文
    username = models.CharField(max_length=32,blank=True,verbose_name='用户名')
    # django admin提示
    password = models.CharField(max_length=60, help_text='pwd')
    email = models.CharField(max_length=60)
    #错误信息  # 注意必须有逗号
    test = models.EmailField(max_length=19,null=True,error_messages={'invalid': '请输入密码',})
    # UserInfo表中没有user_group字段，而是 user_group_id 列 值为 uid 数字
    #user_group = models.ForeignKey("UserGroup",to_field='uid')      # 外键关联 **********
    #不使用外键
    user_group_id= models.IntegerField(null=True)

    class Meta:
        db_table = 't_userinfo'