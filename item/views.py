from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Category
from .forms import NewItemForm

def items(request):
    items = Item.objects.all()
    return render(request, 'items.html',{
        'items': items,
        'title':'All products',
    })

def newItem(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

    else:
        form = NewItemForm()

    return render(request, 'newItem.html', {
        'form': form,
    })

def detail(request, name):
    item = get_object_or_404(Item, name=name)
    return render(request, 'detail.html', {
        'item':item,
    })

def search(request):
    query = request.GET.get('query', '')
    items = Item.objects.all()

    if query:
        items = items.filter(name__contains=query)
    else:
        return redirect('core:home')

    return render(request, 'items.html', {
        'items': items,
        'query': query,
        'title':query,
    })

def category(request, name):
    category = get_object_or_404(Category, name=name)
    items = Item.objects.filter(category=category)
    title = category.name
    return render(request, 'items.html',{
        'category': category,
        'items': items,
        'title': title,
    })