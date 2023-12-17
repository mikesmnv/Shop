from django.contrib import admin
from .models import Article

admin.site.register(Article)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = 'title'
    search_fields = ('title', 'content')

# Register your models here.
