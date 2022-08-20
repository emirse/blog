from django.contrib import admin
from django.urls import path,re_path
from .views import category_show,show_item,search

urlpatterns = [
    path("search/", search, name="search"),
    path('<slug:category_slug>/', category_show, name="category_show"),
    path('category-item/<slug:category_item_slug>/', show_item, name="show_item"),

]
