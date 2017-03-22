from django.contrib import admin

# Register your models here.

from .models import Post 

class PostAdmin (admin.ModelAdmin):
	list_display = ['title', 'slug', 'container', 'created', 'modified']
	search_fields = ['title', 'slug']
	list_filter = ['created', 'modified']

admin.site.register (Post, PostAdmin)