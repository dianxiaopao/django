# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from dataAPI import api_response
from sclass.models import SclassCourseRel
from sclass.serializers import SclassCourseRelSerializer

class SclassList(APIView):
    def post(self, request, format=None):
        # 可以获取 post  raw/form-data类型的数据
        # print  type(data)
        params = request.data.get('1',None)
        if params is None:
            # return Response({'data': '{}', 'err_code': '1', 'err_desc': '参数不能为空'}, status=status.HTTP_200_OK)
            return api_response.JsonResponse(data=None, code='1', desc='参数不能为空')  # 使用上面的进行返回
        queryset = SclassCourseRel.objects.raw(
                                    '''SELECT ssr.*  from 
                                      t_sclass_student_rel ssr,t_sclass_course_rel scr 
                                      WHERE scr.teacher_id ='1' 
                                      and scr.sclass_id = ssr.sclass_id
                                      ''')
        print type(queryset)

        data = json.dumps(queryset)
        print data
        serializer =SclassCourseRelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        #return api_paginator.api_paging(queryset, None, None,StudentSerializer)  # 分页处理，并返回
      #  return api_paginator.api_paging(queryset, params.get('page_size',None), params.get('page',None),StudentSerializer)  # 分页处理，并返回
