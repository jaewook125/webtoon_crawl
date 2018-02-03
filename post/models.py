from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

class Webtoon(models.Model):
	title = models.CharField(max_length=100, verbose_name='제목')
	image = models.ImageField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title


class Detail(models.Model):
	webtoon = models.ForeignKey(Webtoon, on_delete=models.CASCADE)
	image = models.ImageField(verbose_name='Detail')
