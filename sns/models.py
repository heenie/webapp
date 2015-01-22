from django.db import models


class Student(models.Model):
    AREA_CHOICES = [(0, "기숙사"), (1, "양덕동"), (2, "장흥초"), (3, "환호동"), (4, "육거리"), (5, "기타")]

    stu_id = models.CharField(unique=True, max_length=8, min_length=8)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    area = models.IntegerField(choices=AREA_CHOICES)
    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(upload_to="/student", default="defaults/avatar.png")      #static 폴더


class Category(models.Model):
    CATEGORY_CHOICES = [(0, "맛집"), (1, "공동구매"), (2, "생활"), (3, "부동산"), (4, "카풀"), (5, "기타")]

    name = models.IntegerField(choices=CATEGORY_CHOICES)


class Article(models.Model):
    number = models.IntegerField()
    datetime = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(Student)
    category = models.ForeignKey(Category)
    content = models.TextField()