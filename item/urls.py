from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('items/', views.items, name='items'),
    path('new/item/', views.newItem, name='newItem'),
    path('detail/<str:name>', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    path('category/<str:name>', views.category, name='category'),
]