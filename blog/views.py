from django.shortcuts import render
from django.shortcuts import redirect
from .models import Post, Tag
from .utils import *
from django.views.generic import View
from .forms import TagForm, PostForm

def main_view(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create_form.html'
    # def get(self, request):
    #     form = PostForm()
    #     return render(request, 'blog/post_create_form.html', context={'form': form})
    #
    # def post(self, request):
    #     bound_form = PostForm(request.POST) #здесь в POST мы передаем наши токен + поля можно глянуть через несколько принтов
    #
    #     if bound_form.is_valid():  # если наша форма валидна
    #         new_tag=bound_form.save() #сохрани данные
    #         return redirect(new_tag) # перенаправь
    #     return render(request, 'blog/post_create_form.html', context={'fomr': bound_form})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'
    # def get(self, request):
    #     form = TagForm()
    #     return render(request, 'blog/tag_create.html', context={'form': form})
    #
    # def post(self, request):
    #     bound_form = TagForm(request.POST) #здесь в POST мы передаем наши токен, title, slug. можно глянуть через несколько принтов
    #
    #     if bound_form.is_valid():  # если наша форма валидна
    #         new_tag=bound_form.save() #сохрани данные
    #         return redirect(new_tag) # перенаправь
    #
    #     return render(request, 'blog/tag_create.html', context={'form': bound_form})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags':tags})
