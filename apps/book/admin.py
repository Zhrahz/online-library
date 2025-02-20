from django.contrib import admin

from apps.book.models import Book, Comment


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display= ['title','author']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['book','user','comment','score']