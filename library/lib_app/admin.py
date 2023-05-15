from django.contrib import admin
from .models import Book, booktype

# Register your models here.
admin.site.register(Book)
admin.site.register(booktype)