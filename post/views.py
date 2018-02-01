from django.shortcuts import render
from post.models import Webtoon

def webtoon_list(request):
	qs = Webtoon.objects.all()

	return render(request, 'post/webtoon_list.html', {
										"post":qs
		})