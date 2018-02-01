from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

class Webtoon(models.Model):
	title = models.CharField(max_length=100)
	image = ProcessedImageField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title