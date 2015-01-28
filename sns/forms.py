from django import forms
from django.contrib.auth.forms import UserCreationForm
from sns.models import *


class JoinForm(UserCreationForm):
    phone = forms.CharField(max_length=20)
    area = forms.ModelChoiceField(queryset=Area.objects)
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ("last_name", "first_name", "username", "password1", "password2", "phone", "email", "area", "image")

    def save(self, commit=True):
        user = super(JoinForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.save()
        student = Student(user=user, contact=self.cleaned_data['phone'], area=self.cleaned_data['area'], image=self.cleaned_data['image'])
        student.save()
        return user



