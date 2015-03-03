# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from webapp import settings


class Area(models.Model):
    name = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.name


class Trade(models.Model):
    total_fee = models.IntegerField(null=True, blank=True)
    per_fee = models.IntegerField(null=True, blank=True)
    time = models.DateTimeField(auto_now=False)
    now_num = models.IntegerField(null=True, blank=True)
    total_num = models.IntegerField(null=True, blank=True)
    memo = models.TextField()


class Car(models.Model):
    depart = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    transportation = models.CharField(max_length=50)
    trade = models.ForeignKey(Trade)


class Store(models.Model):
    title = models.CharField(max_length=50)
    trade = models.ForeignKey(Trade)
    link = models.CharField(max_length=200)


class House(models.Model):
    title = models.CharField(max_length=50)
    area = models.ForeignKey(Area)
    sell_mon = models.IntegerField(null=True, blank=True)
    sell_deposit = models.IntegerField(null=True, blank=True)
    roommate = models.BooleanField(default=False)
    room_mon = models.IntegerField(null=True, blank=True)
    room_deposit = models.IntegerField(null=True, blank=True)
    time = models.DateTimeField(auto_now=False)
    memo = models.TextField()


class Student(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=20, null=True, blank=True)
    is_public = models.BooleanField(default=False)
    area = models.ForeignKey(Area)
    image = models.ImageField(upload_to="./profile", null=True, blank=True)

    def __str__(self):
        return self.get_name() + "(" + self.user.get_username() + ")"

    def get_name(self):
        return self.user.last_name + self.user.first_name

    def get_phone(self):
        phone = self.phone if self.is_public else "010-xxxx-xxxx"
        return phone

    def get_image(self):
        return self.image if self.image else settings.DEFAULT_PROFILE


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Article(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(Student)
    category = models.ForeignKey(Category)
    content = models.TextField()
    car = models.ForeignKey(Car, null=True)
    store = models.ForeignKey(Store, null=True)
    house = models.ForeignKey(House, null=True)

    def __str__(self):
        return "게시글" + str(self.id)

    def get_comments(self):
        return Comment.objects.filter(article=self)


class Image(models.Model):
    image = models.ImageField(upload_to="./image", null=True, blank=True)
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