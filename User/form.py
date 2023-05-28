from time import timezone

from django import forms
from .models import User, Task, Submission


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


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content', 'deadLine']

    def clean(self):
        cleaned_data = super().clean()
        end_time = cleaned_data.get('deadLine')
        if end_time and end_time < timezone.now():
            raise forms.ValidationError('Submission deadline has passed.')

class DocumentForm(forms.Form):
    name = forms.CharField(max_length=50)
    student_id = forms.CharField(max_length=20)
    document = forms.FileField()


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['task', 'file']

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            return file
        else:
            raise forms.ValidationError('请选择一个文件！')


class UserFormLogin(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
