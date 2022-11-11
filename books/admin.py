from django.contrib import admin
from .models import Book, BookAuthor, Author, Review


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description')
    list_display = ('title', 'descriptions', 'isbn')


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name',)
    list_display = ('first_name', 'last_name', 'email')


class BookAuthorAdmin(admin.ModelAdmin):
    search_fields = ('book_id', 'author_id')


class ReviewAdmin(admin.ModelAdmin):
    search_fields = ('stars_given', 'review_text',)
    list_display = ('review_text', 'stars_given')


admin.site.register(Book, BookAdmin)
admin.site.register(BookAuthor, BookAuthorAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Review, ReviewAdmin)