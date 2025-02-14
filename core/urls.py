from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # 首頁
    path('', views.home, name='home'),
    
    # 教學資源
    path('resources/', views.ResourceListView.as_view(), name='resource_list'),
    path('resources/<int:pk>/', views.ResourceDetailView.as_view(), name='resource_detail'),
    path('resources/create/', views.ResourceCreateView.as_view(), name='resource_create'),
    
    # 教學影片
    path('videos/', views.VideoListView.as_view(), name='video_list'),
    path('videos/<int:pk>/', views.VideoDetailView.as_view(), name='video_detail'),
    
    # 練習題
    path('exercises/', views.ExerciseListView.as_view(), name='exercise_list'),
    path('exercises/<int:pk>/', views.ExerciseDetailView.as_view(), name='exercise_detail'),
    
    # 討論區
    path('forum/', views.ForumListView.as_view(), name='forum'),
    path('forum/post/<int:pk>/', views.ForumPostDetailView.as_view(), name='post_detail'),
    path('forum/post/create/', views.ForumPostCreateView.as_view(), name='post_create'),
    
    # 用戶相關
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register, name='register'),
]
