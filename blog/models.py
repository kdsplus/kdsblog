#-*- coding: utf-8 -*-

# from or import 로 시작되는 부분은 다른 파일에 있는 것을 추가하라는 의미임
#from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

# 모델 정의 class ModelName Class 첫 글자는 대문자로 시작함
# models.Model 은 장고 모델을 의미함 이 코드로 인하여 장고는 Post가 데이터 베이스에 저장되어야 한다는 것을 인식함
# models.CharField - Char 속성의 필드
# models.TextFiedl - Text, Memo와 같은 긴 텍스트를 위한 속성 필드
# models.DateTiemField - 날짜시간 속성의 필드
# models.ForeignKey - 다른 모델에 대한 링크
# cf > https://docs.djangoproject.com/en/1.8/ref/models/fields/#field-types
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.text
