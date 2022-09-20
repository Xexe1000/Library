from django.contrib import admin
from django.contrib.admin import TabularInline
from django.db.models import Avg
from modeltranslation.admin import TranslationAdmin
from Book.models import Book, Genre, File, Favorite, Rating, Like, Comment


@admin.register(Book)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "type", "average_rating")

    def average_rating(self, obj):
        from Book.models import Rating
        result = Rating.objects.filter(book=obj).aggregate(Avg('star'))
        return result.get('star__avg')


# @admin.register(Book)
# class SelectionModelAdmin(TranslationAdmin):
#     readonly_fields = ['id']
#     list_display = ['type', 'genre', 'description', 'name', 'author']


# admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(File)
admin.site.register(Favorite)
admin.site.register(Rating)
admin.site.register(Like)
admin.site.register(Comment)
