from django.shortcuts import render, get_object_or_404
from .models import *
from django.shortcuts import redirect
from django.urls import reverse


class ObjectDetailMixin:  # миксин который дает метод, который дает "детали" объекта,
                          # метод get это метод из под копота, и его не надо вызывать
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template,
                      context={self.model.__name__.lower(): obj})


class ObjectCreateMixin:
    form_model = None
    template = None

    def get(self, request):
        form = self.form_model()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.form_model(request.POST) #здесь в POST мы передаем наши токен, title, slug. можно глянуть через несколько принтов

        if bound_form.is_valid():  # если наша форма валидна
            new_tag=bound_form.save() #сохрани данные
            return redirect(new_tag) # перенаправь

        return render(request, self.template, context={'form': bound_form})

class ObjectUpdateixin:
    model = None
    model_form = None
    template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug) #достаем по слагу тег
        bound_form = self.model_form(instance=obj) #заполняем форму данными этого тега
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug) #достаем по слагу тег
        bound_form = self.model_form(request.POST, instance=obj) #заполняем форму данными этого тега

        if bound_form.is_valid(): #если валидна
            new_obj = bound_form.save() #перезапиши данные
            return redirect(new_obj)  # перенаправь на новые данные
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})


class ObjectDeleteMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse('main_url'))
