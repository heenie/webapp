# -*- coding: utf-8 -*-
from datetime import datetime, date, timedelta
from django.utils.timesince import timesince
from django.contrib.auth.models import User
from django.db import models


class Area(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=20, null=True, blank=True)
    is_public = models.BooleanField(default=False)
    area = models.ForeignKey(Area)
    image = models.ImageField(upload_to="profile", null=True, blank=True)

    def __str__(self):
        return self.get_name() + "(" + self.user.get_username() + ")"

    def get_name(self):
        return self.user.last_name + self.user.first_name

    def get_phone(self):
        phone = self.phone if self.is_public else "010-xxxx-xxxx"
        return phone

    def get_image(self):
        return self.image if self.image else "profile/default/avatar.png"


class Category(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30, default="default")

    def __str__(self):
        return self.name


class Article(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(Student)
    category = models.ForeignKey(Category)
    content = models.TextField()

    def __str__(self):
        return "게시글" + str(self.id)

    def get_datetime(self):
        if (self.datetime.date() + timedelta(days=1)) == date.today():
            return timesince(self.datetime) + " 전"
        else:
            return self.datetime.date() + timedelta(days=1)

    def get_comments(self):
        return Comment.objects.filter(article=self)

        # def get_main_image(self):
        #     if self.entryfile_set.all().exists():
        #         return self.entryfile_set.all()[0].file
        #     else:
        #         return None


class Trade(models.Model):
    fee = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    memo = models.TextField(null=True, blank=True)


class Car(models.Model):
    depart = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    transportation = models.CharField(max_length=50)
    trade = models.OneToOneField(Trade)
    article = models.OneToOneField(Article)


class Store(models.Model):
    title = models.CharField(max_length=50)
    link = models.URLField(null=True)
    trade = models.OneToOneField(Trade)
    article = models.OneToOneField(Article)


class House(models.Model):
    title = models.CharField(max_length=50)
    area = models.ForeignKey(Area)
    trade = models.OneToOneField(Trade)
    article = models.OneToOneField(Article)


class Image(models.Model):
    image = models.FileField(upload_to='documents/%Y/%m/%d', null=True, blank=True)
    article = models.ForeignKey(Article)


class Comment(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(Student)
    article = models.ForeignKey(Article)
    content = models.CharField(max_length=400)

    def __str__(self):
        return "댓글" + str(self.id) + "(" + str(self.article) + ")"
