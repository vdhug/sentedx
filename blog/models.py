from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=64)
	body = models.TextField(default="")
	date = models.DateTimeField()

	def __str__(self):
		return self.title;
