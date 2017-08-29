# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from rest_framework.views import APIView
from student.models import Student,StudentSorce
from student.serializers import StudentSerializer,StudentSorceSerializer
from rest_framework.response import Response
from rest_framework import status
# 简单方式
# class StudentList(generics.ListCreateAPIView):
#      queryset = Student.objects.all()
#      serializer_class = StudentSerializer

#复杂方式
class StudentList(APIView):
    def get(self, request, format=None):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        dict = {'code': 0000, 'data': serializer.data, 'msg': "success"}
        return Response(dict)

    # def post(self, request, format=None):
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 简单方式 单个学生
# class StudentDetail(generics.RetrieveUpdateAPIView):
#     serializer_class = StudentSerializer
#     queryset = Student.objects.all()
#     # 得到一个数据集
#     def get_queryset(self):
#         return Student.objects.filter(name=self.kwargs['name'])
#
#     # get方法返回一个student
#     def get(self, request, *args, **kwargs):
#         # 获取url中的参数
#         # http://127.0.0.1:8000/api/students/aaa/?test=123
#         # 取test的值
#         print(self.request.GET.get('test', None))
#
#         queryset = self.get_queryset()
#         for blog in queryset:
#             print blog.name;
#         serializer = StudentSerializer(queryset, many=True)
#         return Response({
#             'data': serializer.data,
#             #'sorce': StudentSorceSerializer(StudentSorce.objects.all(), many=True).data
#         })
#
#     # 更新某一个学生的信息
#     def update(self, request, *args, **kwargs):
#         pass
#复杂方式
class StudentDetail(APIView):
    # 得到一个数据集
    def get_queryset(self):
        return Student.objects.filter(name=self.kwargs['name'])

    # get方法返回一个student
    def get(self, request,format=None,*args, **kwargs):
        queryset = self.get_queryset()
        for blog in queryset:
            print blog.name;
        serializer = StudentSerializer(queryset, many=True)
        return Response({
            'data': serializer.data,
            #'sorce': StudentSorceSerializer(StudentSorce.objects.all(), many=True).data
        })

    def post(self, request, format=None):
        print(request.data['name'])
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


