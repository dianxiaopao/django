# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from rest_framework.views import APIView
from student.models import Student,StudentSorce
from student.serializers import StudentSerializer,StudentSorceSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from dataAPI import  api_response,api_paginator
# 简单方式
# class StudentList(generics.ListCreateAPIView):
#      queryset = Student.objects.all()
#      serializer_class = StudentSerializer

#复杂方式
class StudentList(APIView):
    def get(self, request, format=None):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        #dict = {'code': 0, 'data': serializer.data, 'msg': "success"}
        return api_response.JsonResponse(data=serializer.data, code=status.HTTP_200_OK, desc='ok') #使用上面的进行返回

    # def post(self, request, format=None):
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#学生列表，分页
class StudentListPaginator(APIView):
    def post(self, request, format=None):
        # 可以获取 post  raw/form-data类型的数据
        data = request.data
        # print  type(data)
        names = data.get('1',None)
        queryset = Student.objects.all()
        return api_paginator.api_paging(queryset, request, StudentSerializer)  # 分页处理，并返回


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
        })

    def post(self, request, format=None):
       # data = request.data  等同于下面的代码  最终通过json.load方法得带json对象  dict  dict 使用get方法 防止 娶不到key而抛出异常
       # data = JSONParser().parse(request)
       #可以获取 post  raw/form-data类型的数据
        data = request.data
       # print  type(data)
        names=data.get('name',default=None)
       #或者
        names = data.get('name', None)
       # print 'postdata is ' + names
        if names is None :
            #return Response({'data': '{}', 'err_code': '1', 'err_desc': '参数不能为空'}, status=status.HTTP_200_OK)
             return api_response.JsonResponse(data=None, code='1', desc='参数不能为空')  # 使用上面的进行返回
        queryset=Student.objects.filter(name=names)
        serializer = StudentSerializer(queryset, many=True)
        return api_response.JsonResponse(data=serializer.data, code=status.HTTP_200_OK, desc='ok')  # 使用上面的进行返回


