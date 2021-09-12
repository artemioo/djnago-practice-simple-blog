from django import forms
from .models import Tag, Post
from django.core.exceptions import ValidationError

class TagForm(forms.ModelForm):  #ModelForm вместо Form расширяет наш функционал
    # title = forms.CharField(max_length=50)
    # slug = forms.CharField(max_length=50)
    #
    # title.widget.attrs.update({'class': 'form-control'})
    # slug.widget.attrs.update({'class': 'form-control'})
    class Meta:  # связывание
        model = Tag
        fields = ['title', 'slug'] #мы должны использовать такие поля: , но можно и '__all__', но это bad practice

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-contol'}),
            'slug': forms.TextInput(attrs={'class': 'form-contol'})
        }


    def clean_slug(self): #clean_ это соглашение джанго, должен начинатся так, а дальше поле форме которое должен валидировать этот метод
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        if Tag.objects.filter(slug__iexact=new_slug).count(): #filter вернет QuerySet, по данным значениям, а count их посчитает
            raise ValidationError('Slug must be unique.')     # но если их > 0 возбуди ошибку
        return new_slug


    # def save(self):  такой метод нам не нужен потому что он есть у ModelForm
    #     new_tag = Tag.objects.create(
    #         title=self.cleaned_data['title'],
    #         slug=self.cleaned_data['slug'])
    #     return new_tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']

        widgets = {
        'title': forms.TextInput(attrs={'class': 'form-contol'}),
        'slug': forms.TextInput(attrs={'class': 'form-contol'}),
        'body': forms.Textarea(attrs={'class': 'form-contol'}),
        'tags': forms.SelectMultiple(attrs={'class': 'form-contol'})
        }
    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        return new_slug
