# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from uuid import uuid4
from django.utils.deconstruct import deconstructible
from django.conf import settings

@deconstructible
class PathAndRename(object):
    def __init__(self, path):
        self.sub_path = path
    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.sub_path, filename)

class User(models.Model):
    createdate = models.DateTimeField(auto_now_add=True)
    updatedate = models.DateTimeField(auto_now=True)
    account = models.CharField(blank=False, max_length=20, unique=True)
    password = models.CharField(blank=False, max_length=20)
    name = models.CharField(blank=True, null=True, max_length=20, default="")
    email = models.EmailField(unique=True)
    position = models.CharField(blank=True, null=True, max_length=20, default="")
    company = models.CharField(blank=True, null=True, max_length=60, default="")

class Account(models.Model):
    createdate = models.DateTimeField(auto_now_add=True)
    updatedate = models.DateTimeField(auto_now=True)
    uid = models.IntegerField()
    credit = models.CharField(blank=False, max_length=30)
    balance = models.IntegerField(default=0)
