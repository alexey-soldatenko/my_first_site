from django.db import models
from django.utils import timezone

# Create your models here.

class Part(models.Model):
	name_part = models.CharField(max_length=100, default='other')

	def __str__(self):
		return self.name_part

class Articles(models.Model):
	part = models.ForeignKey(Part)
	url_name = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	context = models.TextField()
	date_publicate = models.DateField()

	def __str__(self):
		return self.title

class Comments(models.Model):
	context = models.TextField()
	user_name = models.CharField(max_length=100)
	article_name = models.CharField(max_length=50)
	date = models.DateField(default=timezone.now)

	def __str__(self):
		return 'comments'
