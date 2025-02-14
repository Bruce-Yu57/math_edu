from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Resource, Video, Exercise, ForumPost

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'user_type', 'password1', 'password2']
        labels = {
            'username': '用戶名',
            'email': '電子郵件',
            'user_type': '用戶類型',
            'password1': '密碼',
            'password2': '確認密碼',
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'bio', 'avatar']
        labels = {
            'username': '用戶名',
            'email': '電子郵件',
            'bio': '個人簡介',
            'avatar': '頭像',
        }

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'description', 'file', 'resource_type', 'subject']
        labels = {
            'title': '標題',
            'description': '描述',
            'file': '檔案',
            'resource_type': '資源類型',
            'subject': '科目',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'url', 'subject']
        labels = {
            'title': '標題',
            'description': '描述',
            'url': '影片連結',
            'subject': '科目',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['title', 'content', 'answer', 'explanation', 'subject', 'difficulty']
        labels = {
            'title': '標題',
            'content': '題目內容',
            'answer': '答案',
            'explanation': '解析',
            'subject': '科目',
            'difficulty': '難度',
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
            'answer': forms.Textarea(attrs={'rows': 2}),
            'explanation': forms.Textarea(attrs={'rows': 4}),
        }

class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['title', 'content']
        labels = {
            'title': '標題',
            'content': '內容',
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 6}),
        }
