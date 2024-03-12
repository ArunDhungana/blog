from django.shortcuts import get_object_or_404, render, redirect
from .models import BlogpostModel
from .forms import  CategoryForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import CategoryModel
from .forms import CategoryForm

@login_required
def home(request):
    blogpost_objs = BlogpostModel.objects.all()
    context = {
        "blogposts":blogpost_objs
    }
    # print(blogpost_objs.image.)
    return render(request, 'home.html', context)

@login_required
def category_list(request):
    categories = CategoryModel.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

@login_required
def category_detail(request, pk):
    category = get_object_or_404(CategoryModel, pk=pk)
    return render(request, 'category_detail.html', {'category': category})

@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})

@login_required
def category_update(request, pk):
    category = get_object_or_404(CategoryModel, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(CategoryModel, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category_confirm_delete.html', {'category': category})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})