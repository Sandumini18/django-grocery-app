from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignUpForm

def home(request):
    categories = Category.objects.all()[0:5]
    items = Item.objects.all()[0:5]
    return render(request, 'core/home.html',{
        'categories':categories,
        'items':items,
    })

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form = SignUpForm()
        
    return render(request, 'core/signup.html',{
        'form': form,
    })