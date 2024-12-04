from django.contrib import admin

from .models import Author, Book


@admin.register(Author)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'middle_name', 'description')
    search_fields = ('last_name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'publication_date', 'author')
    search_fields = ('title', 'author__last_name')