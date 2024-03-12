from django import forms
from .models import BlogpostModel
from .models import CategoryModel

class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = ['title', 'description']

from .models import BlogpostModel

class BlogpostForm(forms.ModelForm):
    class Meta:
        model = BlogpostModel
        fields = ['title', 'image', 'author', 'category', 'content']