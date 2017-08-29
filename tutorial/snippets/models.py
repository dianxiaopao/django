# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import  models
from pygments.lexers import  get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    #如果为True，字段允许为空，默认不允许
    code = models.TextField(blank=True)
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)

if __name__ == "__main__":
    #我想让着两个list中的偶数分别相加，应该结果是2 + 6, 4 + 6, 2 + 8, 4 + 8
    # x = [1, 2, 3, 4]
    # y = [5, 6, 7, 8]
    # print([a + b for a in x for b in y if a % 2 == 0 and b % 2 == 0])
    # print (LEXERS2)
    print (LANGUAGE_CHOICES)# print(get_all_lexers())
    #for item in LANGUAGE_CHOICES:
        #print item

