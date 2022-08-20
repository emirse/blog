from django.shortcuts import get_object_or_404, render
from topic.models import Category, CategoryItem
from django.db.models import Q
STATUS='published'

def search(request):
   print("Buradayım search")
   context = dict()
   if request.method == 'GET':
      # use input field name to get the search text
      query = request.GET.get('search')
      context['items'] = CategoryItem.objects.filter(title__icontains=query)
   return render(request, 'topic/category_show.html', context)


def category_show(request,category_slug):
    context = dict()
    print("Buradayım show")
    context['category']=get_object_or_404(Category,slug=category_slug)
    print("cccc",context['category'])
    context['items'] = CategoryItem.objects.filter(
        category=context['category'],
        status=STATUS,
    )
    print("dsadsadasd" ,context['items'])
    return render(request, 'topic/category_show.html', context)


def show_item(request, category_item_slug):
    context = dict()
    
    context['category'] = get_object_or_404(
        CategoryItem, slug=category_item_slug)
    print("cccc",context['category'])
    context['items'] = CategoryItem.objects.filter(
        title=context['category'],
        status=STATUS
    ).order_by('title')
    print("dsadsadasd" ,context['items'])
    return render(request, 'page/page.html', context)




    
    





