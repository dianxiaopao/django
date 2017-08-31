# -*- coding: utf-8 -*-
from users.models import UserGroup, UserInfo
from rest_framework import serializers


class UserInfoSerializer(serializers.ModelSerializer):
    group = serializers.SerializerMethodField('get_user_group')

    class Meta:
        model = UserInfo
        fields = ('username', 'password', 'email', 'test', 'user_group_id','group')

    # 使用学号查出该学生的成绩
    def get_user_group(self, obj):
        print obj.user_group_id
       # 可以同时处理多个UserGroup实例, 只需要在它的构造方法中加入many=True这个参数即可,如下：
        return UserGroupSerializer(UserGroup.objects.filter(uid=obj.id), many=True).data

class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = ('uid', 'caption', 'ctime', 'uptime')