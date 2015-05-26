# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Recruit(models.Model):
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=8)
    is_female = models.BooleanField(default=False)
    birth = models.DateField()
    phone = models.CharField(max_length=20)
    major = models.CharField(max_length=10)
    semester = models.IntegerField()
    major_experience = models.TextField(null=True, blank=True)
    experience = models.TextField(null=True, blank=True)
    major_subject = models.TextField(null=True, blank=True)
    interest = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_fields(self):
        pairs = []
        for field in self._meta.fields:
            name = field.name
            try:
                pairs.append((name, getattr(self, "get_%s_display" % name)()))
            except AttributeError:
                pairs.append((name, getattr(self, name)))
        return pairs