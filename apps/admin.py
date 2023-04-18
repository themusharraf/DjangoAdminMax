from unicodedata import category

from django.contrib import admin
from django.utils.html import format_html
from import_export.admin import ImportExportModelAdmin
from apps.models import Product, Category


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'price', 'category', 'images', 'description', 'created_at')
    fields = ('name', 'price', 'image', 'category', 'description')
    # product narxi buyicha filter qiladi yoki boshqa yozish mumkin
    list_filter = ['price']
    # show products page
    list_per_page = 4

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


"""
Python Backend Ustoz PDP,


models.Tag.objects.update(name=Func(Concat('id', 'name', output_field=CharField()), function='md5'))
models.Tag.truncate()

Python Backend Ustoz PDP,


str(models.Tag.objects.order_by('?').query)

'SELECT "apps_tag"."id", "apps_tag"."name" FROM "apps_tag" ORDER BY RANDOM() ASC'

@classmethod
def truncate(cls):
    with connection.cursor() as cursor:
        cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(cls._meta.db_table))"""