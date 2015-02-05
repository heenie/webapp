from django import forms
from django.contrib.auth.forms import UserCreationForm
from sns.models import *


class SearchForm(forms.Form):
    search = forms.CharField(label="검색", required=False)
    category = forms.ModelChoiceField(queryset=Category.objects)


class WriteForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        exclude = ['datetime', 'student']


class JoinForm(UserCreationForm):
    phone = forms.CharField(max_length=20, label='휴대전화')
    is_public = forms.BooleanField(required=False, label='공개여부')
    area = forms.ModelChoiceField(queryset=Area.objects, label='거주지역')

    class Meta:
        model = User
        fields = ("last_name", "first_name", "username", "password1", "password2", "phone", "is_public", "email", "area")

    def __init__(self, *args, **kwargs):
        super(JoinForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == "last_name" or field_name == "first_name":
                field.widget.attrs['class'] = 'short-text-field'
            elif field_name == "phone":
                field.widget.attrs['class'] = 'medium-text-field'
            elif field_name == "is_public":
                field.widget.attrs['class'] = 'check-box'
            elif field_name == "area":
                field.widget.attrs['class'] = 'drop-down'
            else:
                field.widget.attrs['class'] = 'text-field'
            field.widget.attrs['placeholder'] = field.label

    def save(self, commit=False):
        user = super(JoinForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.save()
        student = Student(user=user, phone=self.cleaned_data['phone'], is_public=self.cleaned_data['is_public'], area=self.cleaned_data['area'])
        student.save()
        return user




