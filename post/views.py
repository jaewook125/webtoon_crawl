from django.shortcuts import render, get_object_or_404
from post.models import Webtoon
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def webtoon_list(request):
	qs = Webtoon.objects.all()

	q = request.GET.get('q', '')
	if q:
		qs = qs.filter(title__icontains=q)

	paginator = Paginator(qs, 9)
	page = request.GET.get('page')
	contacts = paginator.get_page(page)

	return render(request, 'post/webtoon_list.html', {
										"post":qs,
										"contacts":contacts,
		})

def webtoon_detail(request):
	pass