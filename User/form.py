from django import forms
from .models import User


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='密码')
    email = forms.EmailField(required=True, label='电子邮件地址', error_messages={'exists': 'Email已经存在'})
    role_choices = (
        ('teacher', "老师"),
        ('student', "学生"),
    )
    role = forms.ChoiceField(choices=role_choices, label='角色')

    class Meta:
        model = User
        fields = ['email', 'password', 'role']
