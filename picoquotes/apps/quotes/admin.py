from django.contrib import admin

from .models import Author, Quote


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    pass
