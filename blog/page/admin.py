from django.contrib import admin

# Register your models here.
from django.contrib import admin

from page.models import Page

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    list_display=('pk','title','slug', 'status', 'updated_at',)
    list_filter=('status',)
    list_editable=('status',)

admin.site.register(Page,PageAdmin)
