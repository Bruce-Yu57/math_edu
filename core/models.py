from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('teacher', '教師'),
        ('student', '學生'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

class Subject(models.Model):
    name = models.CharField(max_length=100)
    grade = models.IntegerField(choices=[(i, f'{i}年級') for i in range(7, 10)])
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.grade}年級 - {self.name}'

class Resource(models.Model):
    RESOURCE_TYPES = (
        ('lesson_plan', '教案'),
        ('worksheet', '學習單'),
        ('exam', '試卷'),
        ('other', '其他'),
    )
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='resources/')
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPES)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    downloads = models.IntegerField(default=0)

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

    def get_youtube_id(self):
        """獲取YouTube視頻ID"""
        if 'youtube.com' in self.url:
            if 'v=' in self.url:
                return self.url.split('v=')[-1].split('&')[0]
        elif 'youtu.be' in self.url:
            return self.url.split('/')[-1].split('?')[0]
        return ''

    def get_embed_url(self):
        """獲取嵌入式URL"""
        youtube_id = self.get_youtube_id()
        if youtube_id:
            return f'https://www.youtube.com/embed/{youtube_id}'
        return ''

class Exercise(models.Model):
    DIFFICULTY_CHOICES = (
        ('easy', '簡單'),
        ('medium', '中等'),
        ('hard', '困難'),
    )
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    answer = models.TextField()
    explanation = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

class ForumPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

class Comment(models.Model):
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
