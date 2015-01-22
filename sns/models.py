# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models


class Area(models.Model):
    name = models.CharField(max_length=30, default="")

    def __unicode__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User)
    area = models.ForeignKey(Area)
    image = models.ImageField(upload_to="/profile", default="default/avatar.png")


class Category(models.Model):
    name = models.CharField(max_length=30)


class Article(models.Model):
    number = models.IntegerField()
    datetime = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(Student)
    category = models.ForeignKey(Category)
    content = models.TextField()


class Image(models.Model):
    image = models.ImageField(upload_to="/image", null=True, blank=True)
    article = models.ForeignKey("Article")


class Comment(models.Model):
    number = models.IntegerField()
    datetime = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(Student)
    article = models.ForeignKey(Article)
    content = models.CharField(max_length=400)