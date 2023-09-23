from django.contrib import admin
from .models import category,product
# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    list_display = ['Name','slug']
    prepopulated_fields = {'slug':('Name',)}
admin.site.register(category,categoryAdmin)


class productAdmin(admin.ModelAdmin):
    list_display = ['name','price','discription','stock','available','created','updated']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(product,productAdmin)