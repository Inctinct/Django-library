from django.contrib import admin
from .models import Book, BookInstance, Author, Language, Genre
# Register your models here.


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name','date_of_birth','date_of_death')
    search_fields = ('last_name','first_name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','display_genre')
    search_fields = ('title','author__first_name','author__last_name')


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status','borrower','due_back')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Language, LanguageAdmin)