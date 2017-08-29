# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from student.models import Student,StudentSorce
from student.serializers import StudentSerializer,StudentSorceSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class StudentList(generics.ListCreateAPIView):
     queryset = Student.objects.all()
     serializer_class = StudentSerializer



# 单个学生
class StudentDetail(generics.RetrieveUpdateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    # 得到一个数据集
    def get_queryset(self):
        return Student.objects.filter(name=self.kwargs['name'])

    # get方法返回一个student
    def get(self, request, *args, **kwargs):
        # 获取url中的参数
        # http://127.0.0.1:8000/api/students/aaa/?test=123
        # 取test的值
        print(self.request.GET.get('test', None))

        queryset = self.get_queryset()
        for blog in queryset:
            print blog.name;
        serializer = StudentSerializer(queryset, many=True)
        return Response({
            'data': serializer.data,
            #'sorce': StudentSorceSerializer(StudentSorce.objects.all(), many=True).data
        })

    # 更新某一个学生的信息
    def update(self, request, *args, **kwargs):
        pass
