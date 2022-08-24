from django.contrib import admin
from django.contrib.admin import TabularInline

from Book.models import Book, Genre, File

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(File)

