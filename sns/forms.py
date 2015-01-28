from django import forms
from django.contrib.auth.forms import UserCreationForm
from sns.models import *


class JoinForm(UserCreationForm):
    phone = forms.CharField(max_length=20, label='폰 번호')
    is_public = forms.BooleanField(required=False, label='공개여부')
    area = forms.ModelChoiceField(queryset=Area.objects, label='거주지역')

    class Meta:
        model = User
        fields = ("last_name", "first_name", "username", "password1", "password2", "phone", "is_public", "email", "area")

    def save(self, commit=False):
        user = super(JoinForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.save()
        student = Student(user=user, phone=self.cleaned_data['phone'], is_public=self.cleaned_data['is_public'], area=self.cleaned_data['area'])
        student.save()
        return user

