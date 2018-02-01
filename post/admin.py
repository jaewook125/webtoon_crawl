from django.contrib import admin
from post.models import Webtoon 

@admin.register(Webtoon)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title',]
    list_display_links = ('title',)