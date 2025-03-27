from django.contrib import admin
from books_magazines.models import Ebooks, Audiobook, Magazines, Educational_Book

admin.site.register(Ebooks)
admin.site.register(Audiobook)
admin.site.register(Magazines)
admin.site.register(Educational_Book)