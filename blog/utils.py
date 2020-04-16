from django.shortcuts import render, get_object_or_404, redirect
from blog.models import *
from blog.form import *

class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        # post = Post.objects.get(slug__iexact=slug)
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj, 'admin_obj': obj, 'detail': True})

class ObjectCreateMixin:
    model_form = None
    template = None

    def get(self, request):
        form = self.model_form()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.model_form(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:
    model = None
    form = None
    template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form(instance=obj)
        return render(request, self.template, context={'form': bound_form, 'tag': obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = PostForm(request.POST, instance=obj)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form, 'post': obj})

# class ObjectDeleteMixin:
#     model = None
#     template = None
#     redirect_url = None
#
#     def get(self, request, slug):
#         obj = self.model.objects.get(slug__iexact=slug)
#         return render(request, self.template, context={self.model.__name__.lower():obj})
#
#     def post(self, request, slug):
#         obj = self.model.objects.get(slug__iexact=slug)
#         obj.delete()
#         return redirect(reverse(self.redirect_url))

class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={'obj': obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))
