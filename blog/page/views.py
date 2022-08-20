from django.shortcuts import render
from page.models import Page
from topic.views import STATUS
from topic.views import CategoryItem
# Create your views here.


def index(request):
   context = dict()
   context['images'] = CategoryItem.objects.filter(
        status=STATUS
        ).exclude(cover_image="")

   context['items'] = CategoryItem.objects.filter(
        status=STATUS)
  
   return render(request, 'home/index.html',context)

def page_show(request):
   context = dict()

    #Nav:
   context['categories'] = Page.objects.filter(
         status=STATUS
   ).order_by('title')
   return render(request, 'topic/category_show.html', context)
   
