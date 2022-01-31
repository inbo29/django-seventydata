from django.contrib import admin

# Register your models here.
from .models import Blog

# class BlogAdmin(admin.ModelAdmin):
#     list_display = ['id', 'created', 'updated']
    # raw_id_fields = ['author']
    # list_filter = ['created', 'updated', 'author']
    # search_fields = ['text', 'created', 'author__username']
    # ordering = ['-updated','-created']

admin.site.register(Blog)