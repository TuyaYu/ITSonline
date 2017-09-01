
# -*- encoding:utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from django.apps import AppConfig


class OperationConfig(AppConfig):
    name = 'operation'
    verbose_name=u'用户操作'
