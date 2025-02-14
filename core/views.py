from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Resource, Video, Exercise, ForumPost, Subject
from .forms import ResourceForm, VideoForm, ExerciseForm, ForumPostForm, UserRegistrationForm, UserUpdateForm

def home(request):
    """首頁視圖"""
    context = {
        'subjects': Subject.objects.all(),
        'recent_resources': Resource.objects.order_by('-created_at')[:5],
        'popular_videos': Video.objects.order_by('-views')[:5],
        'recent_posts': ForumPost.objects.order_by('-created_at')[:5],
    }
    return render(request, 'core/home.html', context)

class ResourceListView(ListView):
    """教學資源列表視圖"""
    model = Resource
    template_name = 'core/resource_list.html'
    context_object_name = 'resources'
    paginate_by = 12
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        subject = self.request.GET.get('subject')
        resource_type = self.request.GET.get('type')
        if subject:
            queryset = queryset.filter(subject__id=subject)
        if resource_type:
            queryset = queryset.filter(resource_type=resource_type)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = Subject.objects.all()
        context['resource_types'] = Resource.RESOURCE_TYPES
        return context

class ResourceDetailView(DetailView):
    """教學資源詳情視圖"""
    model = Resource
    template_name = 'core/resource_detail.html'

    def get_object(self):
        obj = super().get_object()
        obj.downloads += 1
        obj.save()
        return obj

class ResourceCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """創建教學資源視圖"""
    model = Resource
    form_class = ResourceForm
    template_name = 'core/resource_form.html'
    success_url = reverse_lazy('resource_list')

    def form_valid(self, form):
        form.instance.uploader = self.request.user
        messages.success(self.request, '教學資源上傳成功！')
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.user_type == 'teacher'

class VideoListView(ListView):
    """教學影片列表視圖"""
    model = Video
    template_name = 'core/video_list.html'
    context_object_name = 'videos'
    paginate_by = 12
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        subject = self.request.GET.get('subject')
        if subject:
            queryset = queryset.filter(subject__id=subject)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = Subject.objects.all()
        return context

class VideoDetailView(DetailView):
    """教學影片詳情視圖"""
    model = Video
    template_name = 'core/video_detail.html'

    def get_object(self):
        obj = super().get_object()
        obj.views += 1
        obj.save()
        return obj

class ExerciseListView(ListView):
    """練習題列表視圖"""
    model = Exercise
    template_name = 'core/exercise_list.html'
    context_object_name = 'exercises'
    paginate_by = 12
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        subject = self.request.GET.get('subject')
        difficulty = self.request.GET.get('difficulty')
        if subject:
            queryset = queryset.filter(subject__id=subject)
        if difficulty:
            queryset = queryset.filter(difficulty=difficulty)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = Subject.objects.all()
        context['difficulties'] = Exercise.DIFFICULTY_CHOICES
        return context

class ExerciseDetailView(DetailView):
    """練習題詳情視圖"""
    model = Exercise
    template_name = 'core/exercise_detail.html'

class ForumListView(ListView):
    """討論區列表視圖"""
    model = ForumPost
    template_name = 'core/forum.html'
    context_object_name = 'posts'
    paginate_by = 15
    ordering = ['-created_at']

class ForumPostDetailView(DetailView):
    """討論貼文詳情視圖"""
    model = ForumPost
    template_name = 'core/post_detail.html'

class ForumPostCreateView(LoginRequiredMixin, CreateView):
    """創建討論貼文視圖"""
    model = ForumPost
    form_class = ForumPostForm
    template_name = 'core/post_form.html'
    success_url = reverse_lazy('forum')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, '貼文發布成功！')
        return super().form_valid(form)

def register(request):
    """用戶註冊視圖"""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, '註冊成功！請登入繼續。')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'core/register.html', {'form': form})

@login_required
def profile(request):
    """用戶個人資料視圖"""
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '個人資料更新成功！')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    
    context = {
        'form': form,
        'user_resources': Resource.objects.filter(uploader=request.user).order_by('-created_at')[:5],
        'user_posts': ForumPost.objects.filter(author=request.user).order_by('-created_at')[:5],
    }
    return render(request, 'core/profile.html', context)
