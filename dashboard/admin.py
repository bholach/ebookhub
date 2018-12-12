from django.contrib import admin
from .models import Ebooks, SubCategory, Category
# Register your models here.
admin.site.register(Ebooks)
admin.site.register(SubCategory)
admin.site.register(Category)
