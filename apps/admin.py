from unicodedata import category

from django.contrib import admin
from django.utils.html import format_html
from import_export.admin import ImportExportModelAdmin
from apps.models import Product, Category


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'price', 'category', 'images', 'description', 'created_at')
    fields = ('name', 'price', 'image', 'category','description')
    list_filter = ['price']  # product narxi buyicha filter qiladi yoki boshqa yozish mumkin
    # show products
    list_per_page = 2

    def images(self, obj):
        return format_html(f'''<a href="{obj.image.url}" target="_blank"><img src="{obj.image.url}"
            alt="image" width="100 height="100" style="object-fit : cover;"/></a>''')


# category ga tigishli productlarin chiqarish uchun
class ProductStackedInline(admin.StackedInline):
    model = Product
    min_num = 0
    extra = 2
    max_num = 2


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)
    fields = ('name',)
    # category ga tegishli productlar feilds
    inlines = (ProductStackedInline,)
