# -*- coding: utf-8 -*-
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import AccountSerializer
from django.contrib.auth.models import User
# 注册模块
class AccountDetail(generics.CreateAPIView):
    serializer_class = AccountSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = AccountSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({'data': '{}','err_code':'0','err_desc': '成功'},status=status.HTTP_200_OK)
        print (serializer.errors)
        return Response({'data': '{}','err_code': '1','err_desc': serializer.errors},status=status.HTTP_200_OK)
