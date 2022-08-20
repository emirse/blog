from django.contrib import admin

from topic.models import Category,CategoryItem

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    list_display=('pk','title','slug', 'status', 'updated_at',)
    list_filter=('status',)
    list_editable=('status',)
class CategoryItemAdmin(admin.ModelAdmin):
    list_display=('pk','title','status', 'updated_at',)
    prepopulated_fields = {'slug': ("title",)}
    list_filter=('status',)
    list_editable=('status',)
admin.site.register(Category,CategoryAdmin)
admin.site.register(CategoryItem,CategoryItemAdmin)