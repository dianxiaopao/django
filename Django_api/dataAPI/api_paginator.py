# -*- coding: utf-8 -*-

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework import status

from dataAPI import api_response #自定义的返回格式 JsonResponse


def api_paging(objs, request, Serializer):
    """
    objs : 实体对象
    request : 请求对象
    Serializer : 对应实体对象的序列化
    """
    try:
        page_size = int(request.data.get('page_size', 2))
        page = int(request.data.get('page', 1))
    except (TypeError, ValueError):
        return api_response.JsonResponse(code=status.HTTP_400_BAD_REQUEST, desc='page and page_size must be integer!')
    """
    Paginator.count：所有页面对象总数，即统计object_list中item数目。当计算object_list所含对象的数量时， Paginator会首先尝试调用object_list.count()。如果object_list没有 count() 方法，Paginator
    接着会回退使用len(object_list)。
    Pagnator.num_pages:页面总数。
    pagiator.page_range：页面范围，从1开始，例如[1, 2, 3, 4]。
    
    """
    paginator = Paginator(objs, page_size) # paginator对象
    totalpage = paginator.num_pages #总页数
    totalcount =paginator.count #总记录数
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        objs = paginator.page(1)
    except EmptyPage:
        objs = paginator.page(paginator.num_pages)

    serializer = Serializer(objs, many=True) #序列化操作

    return api_response.JsonResponse(data={
        'page': page,
        'totalpage': totalpage,
        'totalcount':totalcount,
        'detail': serializer.data,
    }, code=status.HTTP_200_OK, desc='page success') #返回