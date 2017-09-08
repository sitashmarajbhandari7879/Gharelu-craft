
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Forum(models.Model):
	name=models.CharField(max_length=50)
	contact=models.CharField(max_length=20)
	address=models.CharField(max_length=50)
	message=models.TextField(max_length=500)

	def __str__(self):
		return self.name