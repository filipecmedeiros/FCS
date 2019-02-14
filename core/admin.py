from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

from .models import Post, Author, Category

class AuthorAdmin (admin.ModelAdmin):
	list_display = ['name']
	search_fields = ['name']

class CategoryAdmin (admin.ModelAdmin):
	list_display = ['name', 'slug']
	search_fields = ['name', 'slug']

class PostAdmin (SummernoteModelAdmin):
	list_display = ['title', 'slug', 'author', 'category', 'container', 'created', 'modified']
	search_fields = ['title', 'slug']
	list_filter = ['created', 'modified']

admin.site.register (Author, AuthorAdmin)
admin.site.register (Category, CategoryAdmin)
admin.site.register (Post, PostAdmin)