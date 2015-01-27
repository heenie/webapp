# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models


class Area(models.Model):
    name = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User)
    contact = models.CharField(max_length=20, blank=True, null=True)
    area = models.ForeignKey(Area)
    image = models.ImageField(upload_to="/profile", default="default/avatar.png")

    def __str__(self):
        return self.get_name() + "(" + self.get_username() + ")"

    def get_name(self):
        return self.user.last_name + self.user.first_name

    def get_username(self):
        return self.user.username

    def get_area(self):
        return self.area.name


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Article(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(Student)
    category = models.ForeignKey(Category)
    content = models.TextField()

    def __str__(self):
        return "게시글" + str(self.id)


class Image(models.Model):
    image = models.ImageField(upload_to="/image", null=True, blank=True)
    article = models.ForeignKey("Article")

    def __str__(self):
        return "사진" + str(self.id) + "(" + str(self.article) + ")"


class Comment(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(Student)
    article = models.ForeignKey(Article)
    content = models.CharField(max_length=400)

    def __str__(self):
        return "댓글" + str(self.id) + "(" + str(self.article) + ")"
