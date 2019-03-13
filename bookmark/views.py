from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Bookmark

# Create your views here.
# FBV : function Base View
# CBV : Class Base View, 이거

class BookmarkLV(ListView):
    model = Bookmark 
    # 반드시 object_list에 데이터를 가지고 bookmark_list.html로 render

class BookmarkDV(DetailView):
    model = Bookmark
    # 반드시 object_list에 데이터를 가지고 bookmark_detail.html로 render