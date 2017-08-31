# -*- coding: utf-8 -*-
from sclass.models import SclassCourseRel, SclassStudentRel
from rest_framework import serializers


class SclassCourseRelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SclassCourseRel
        fields = ('id', 'course_id', 'sclass_id', 'teacher_id', 'create_time')

    def get_stu_ids(self, obj):
        return obj.stuids

class SclassStudentRelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SclassStudentRel
        fields = ('id', 'stu_id', 'sclass_id', 'create_time')

