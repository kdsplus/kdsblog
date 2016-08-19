#-*- coding: utf-8 -*-

from django.contrib import admin
from .models import Post

# Register your models here.

# 관리자 페이지에서 만든 모델을 보려면
# cf https://docs.djangoproject.com/en/1.8/ref/contrib/admin/ 관리자에 대해서~
admin.site.register(Post)