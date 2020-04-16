from django.shortcuts import render, get_object_or_404, redirect
from blog.models import *
from django.views import View
from .utils import *
from .form import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q

def posts(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()

    pagenator = Paginator(posts, 10)
    page_number = request.GET.get('page', 1)
    page = pagenator.get_page(page_number)
    other_page = page.has_other_pages()
    return render(request, 'blog/posts.html', context={'page_object': page, 'other_page': other_page})

# def post_detail(request, slug):
#     post = Post.objects.get(slug__iexact=slug)
#     return render(request, 'blog/post_detail.html', context={'post':post})

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'
    # def get(self, request, slug):
    #     # post = Post.objects.get(slug__iexact=slug)
    #     post = get_object_or_404(Post, slug__iexact=slug)
    #     return render(request, 'blog/post_detail.html', context={'post': post})


def tags(request):
    tags = Tag.objects.all()
    pagenator = Paginator(tags, 2)
    page_number = request.GET.get('page', 1)
    page = pagenator.get_page(page_number)
    other_page = page.has_other_pages()
    return render(request, 'blog/tags.html', context={'page_object': page, 'other_page': other_page})

# def tag_detail(request, slug):
#     tag = Tag.objects.get(slug__iexact=slug)
#     return render(request, 'blog/tag_detail.html', context={'tag':tag})

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'
    # def get(self, request, slug):
    #     # tag = Tag.objects.get(slug__iexact=slug)
    #     tag = get_object_or_404(Tag, slug__iexact=slug)
    #     return render(request, 'blog/tag_detail.html', context={'tag': tag})

class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True

    # def get(self, request):
    #     form = TagForm()
    #     return render(request, 'blog/tag_create.html', context={'form':form})
    #
    # def post(self, request):
    #     bound_form = TagForm(request.POST)
    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #     return render(request, 'blog/tag_create.html', context={'form':bound_form})

class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = PostForm
    template = 'blog/post_create.html'
    raise_exception = True

    # def get(self, request):
    #     form = PostForm()
    #     return render(request, 'blog/post_create.html', context={'form':form})
    #
    # def post(self, request):
    #     bound_form = PostForm(request.POST)
    #     print('__________________________')
    #     print(bound_form)
    #     for i in bound_form:
    #         print(i)
    #     print('======================')
    #     if bound_form.is_valid():
    #         new_post = bound_form.save()
    #         return redirect(new_post)
    #     return render(request, 'blog/post_create.html', context={'form':bound_form})

class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    form = TagForm
    template = 'blog/tag_update.html'
    raise_exception = True

    # def get(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     bound_form = TagForm(instance=tag)
    #     return render(request, 'blog/tag_update.html', context={'form':bound_form, 'tag':tag})
    #
    # def post(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     bound_form = TagForm(request.POST, instance=tag)
    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #     return render(request, 'blog/tag_update.html', context={'form':bound_form, 'tag':tag})


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    form = PostForm
    template = 'blog/tag_update.html'
    raise_exception = True

    # def get(self, request, slug):
    #     post = Post.objects.get(slug__iexact=slug)
    #     bound_form = PostForm(instance=post)
    #     return render(request, 'blog/tag_update.html', context={'form':bound_form, 'tag':post})
    #
    # def post(self, request, slug):
    #     post = Post.objects.get(slug__iexact=slug)
    #     bound_form = PostForm(request.POST, instance=post)
    #     if bound_form.is_valid():
    #         new_post = bound_form.save()
    #         return redirect(new_post)
    #     return render(request, 'blog/post_update', context={'form':bound_form, 'post':post})

class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete.html'
    redirect_url = 'posts_url'
    raise_exception = True

    # def get(self, request, slug):
    #     post = Post.objects.get(slug__iexact=slug)
    #     return render(request, 'blog/post_delete.html', context={'post':post})
    #
    # def post(self, request, slug):
    #     post = Post.objects.get(slug__iexact=slug)
    #     post.delete()
    #     return redirect(reverse('posts_url'))

class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete.html'
    redirect_url = 'tags_list_url'
    raise_exception = True

    # def get(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     return render(request, 'blog/tag_delete.html', context={'tag':tag})
    #
    # def post(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     tag.delete()
    #     return redirect(reverse('tags_list_url'))
