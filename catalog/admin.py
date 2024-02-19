from django.contrib import admin
from .models import Category, Goods, Tag, Parametr
import admin_thumbnails



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'activate', 'created', 'updated', 'url']
    list_filter = ['activate']
    search_fields = ['name', 'description']



@admin_thumbnails.thumbnail('image')
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'activate', 'created', 'updated', 'category']
    list_filter = ['activate', 'category']
    search_fields = ['name', 'description']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Tag)
admin.site.register(Parametr)


admin.site.site_header = 'Kholodov Admin'
admin.site.site_title = 'Kholodov Admin'
admin.site.index_title = 'Welcome to Kholodov Admin Portal'
# Register your models here.
