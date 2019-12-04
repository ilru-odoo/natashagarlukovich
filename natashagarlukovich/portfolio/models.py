from django.db import models

class Image(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(default='Описание')
	keywords = models.CharField(max_length=120, default='Ключевые слова')
	image = models.FileField(null=True, blank=True)
	visible = models.BooleanField(default=1)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


	class Meta:
		ordering = ["-timestamp"]

class Logo(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(default='Logo')
	image = models.FileField(null=True, blank=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	class Meta:
		ordering = ["-timestamp"]