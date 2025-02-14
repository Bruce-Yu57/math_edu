from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Subject, Resource, Video, Exercise, ForumPost, Comment

# 自定義用戶管理界面
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'user_type', 'is_staff')
    list_filter = ('user_type', 'is_staff', 'is_superuser')
    fieldsets = UserAdmin.fieldsets + (
        ('額外信息', {'fields': ('user_type', 'bio', 'avatar')}),
    )

# 註冊模型
admin.site.register(User, CustomUserAdmin)
admin.site.register(Subject)
admin.site.register(Resource)
admin.site.register(Video)
admin.site.register(Exercise)
admin.site.register(ForumPost)
admin.site.register(Comment)
