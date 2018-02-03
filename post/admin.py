from django.contrib import admin
from post.models import Webtoon, Detail

class ImageTabularInline(admin.TabularInline):
	model = Detail

class WebtoonAdmin(admin.ModelAdmin):
	inlines = [ImageTabularInline]
	class Meta:
		model = Webtoon

admin.site.register(Webtoon, WebtoonAdmin)

admin.site.register(Detail)