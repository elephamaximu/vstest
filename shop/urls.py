from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.article_list, name='list'),
    path('insert/', views.article_insert, name='insert'),
    path('delete/', views.article_delete, name='delete'),
    path('update/', views.article_update, name='update'),
]
