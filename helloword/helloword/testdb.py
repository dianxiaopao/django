#coding=utf-8
from django.http import HttpResponse
from blog.models import Test
#数据库操作
def savedb(request):
	test1 = Test(name='zhangbin')
	test1.save()
	return HttpResponse("数据添加成功！")
def querydb(request):
	 # 初始化
    response = ""
    response1 = ""
     # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list=Test.objects.all()
     # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 =Test.objects.filter(id=1)
    response3 = Test.objects.get(id=1)
    for var in list:
    	#print var.name
    	response1+= var.name+"___"
    response = response1
    for e in response2:
        print('response2='+e.name)
    # 获取单个对象
    print('response3='+response3.name)
     # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    response4 = Test.objects.order_by('name')[0:2]
    for e in response4:
        print('response4='+e.name)
      #数据排序
    response5 =Test.objects.order_by("id")
    for e in response5:
        print('response5='+e.name)
    # 上面的方法可以连锁使用
    response6 = Test.objects.filter(name="zhangbin").order_by("id")
    for e in response6:
        print('response6='+e.name)
    return HttpResponse("<p>" + response + "</p>")
def updatedb(request):
    #修改
    Test.objects.filter(name='22').update(name='我被修改了')
    #修改所有的列
    Test.objects.all().update(name="我的一起修改了")
    return HttpResponse("<p>更新成功</p>")
    # r1=Test.objects.filter(id=1)
    # # for e in r1:
    # 	# print e
    # return HttpResponse("<p></p>")
	#Test.objects.filter(id=1).update(name='Google')
def deletedb(request):
    #删除 单挑
    #Test.objects.filter(id=1).delete();
    #删除所有
    Test.objects.all().delete();
    return HttpResponse("<p>删除成功了</p>")


