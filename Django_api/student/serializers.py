# -*- coding: utf-8 -*-
from student.models import Student, StudentSorce
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    sorce = serializers.SerializerMethodField('get_student_sorce')

    class Meta:
        model = Student
        fields = ('id', 'student_id', 'name', 'age', 'sorce')

    # 使用学号查出该学生的成绩
    def get_student_sorce(self, obj):
        print obj.student_id
       # 可以同时处理多个Snippet实例, 只需要在它的构造方法中加入many=True这个参数即可,如下：
        return StudentSorceSerializer(StudentSorce.objects.filter(student_id=obj.student_id), many=True).data

class StudentSorceSerializer(serializers.ModelSerializer):
    #自定义列，get_avg_sorce方法在 类中定义
    avg = serializers.SerializerMethodField('get_avg_sorce')

    class Meta:
        model = StudentSorce
        fields = ('math', 'english', 'chiness', 'avg')

    # 自定义方法构造的字段(计算成绩的平均值)
    def get_avg_sorce(self, obj):
        return (obj.math + obj.english + obj.chiness) / 3.0
