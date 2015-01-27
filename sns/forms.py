from django import forms
from django.contrib.auth.forms import UserCreationForm
from sns.models import *


class JoinForm(UserCreationForm):
    contact = models.CharField(max_length=20, blank=True, null=True)
    area = models.ForeignKey(Area, name='거주지역')
    image = models.ImageField(upload_to="/profile", default="default/avatar.png")

    class Meta:
        model = User
        fieldsets = ("last_name", "first_name", "username", "password", "contact", "email", "area", "image")

    def save(self, commit=True):
        user = super(JoinForm, self).save(commit=True)
        user.email = self.cleaned_data["email"]
        user.save()
        student = Student(user=user, contact=self.cleaned_data['contact'], area=self.area, image=self.image)
        student.save()
        return user


