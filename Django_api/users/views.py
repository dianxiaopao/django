# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from dataAPI import api_response, api_paginator
from users.models import UserInfo
from users.serializers import UserInfoSerializer


class  UserListPaginator(APIView):
    def post(self, request, format=None):
        # 可以获取 post  raw/form-data类型的数据
        # print  type(data)
        params = request.data.get('1',None)
        if params is None:
            return api_response.JsonResponse(data=None, code='1', desc='参数不能为空')  # 使用上面的进行返回
        queryset = UserInfo.objects.all()
        #return api_paginator.api_paging(queryset, None, None,StudentSerializer)  # 分页处理，并返回
        return api_paginator.api_paging(queryset, params.get('page_size',None), params.get('page',None),UserInfoSerializer)  # 分页处理，并返回


