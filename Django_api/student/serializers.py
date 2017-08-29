# -*- coding: utf-8 -*-
from student.models import Student
from rest_framework import serializers
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'student_id', 'name', 'age')