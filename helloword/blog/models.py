# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Test(models.Model):
	name=models.CharField(max_length=20)
class Contact(models.Model):
	name=models.CharField(max_length=20)
	age=models.CharField(max_length=20)
	email=models.EmailField(max_length=20)
	def __unicode__(self):
		return self.email
class Tag(models.Model):
	contact=models.ForeignKey(Contact)
	name=models.CharField(max_length=50)
	def __unicode__(self):
		return  self.name

# Create your models here.
