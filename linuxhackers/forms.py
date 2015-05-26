from django import forms
from linuxhackers.models import *


class RecruitForm(forms.ModelForm):
    class Meta:
        model = Recruit
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(RecruitForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = '이름 *'
        self.fields['username'].label = '학번 *'
        self.fields['birth'].label = '생년월일 *'
        self.fields['phone'].label = '연락처 *'
        self.fields['major'].label = '1전공 & 2전공 *'
        self.fields['semester'].label = '학기 수 *'
        self.fields['major_experience'].label = '전전 관련 경험'
        self.fields['experience'].label = '교내 활동 경험'
        self.fields['major_subject'].label = '전전 수강 과목'
        self.fields['interest'].label = '전전 관심 분야'