
from django.contrib import admin

from .models import Division,Member





class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name', 'working_as','division','phonenumber']
    list_filter=['division']
    ordering = ['division']

admin.site.register(Division)
admin.site.register(Member,ArticleAdmin)

