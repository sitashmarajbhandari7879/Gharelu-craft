
from __future__ import unicode_literals

from django.db import models

TYPES=(('Pashmina','Pashmina'),
	('Garland','Garland'),
	('Homemade product','Homemade product'),

	('Woolen','Woolen'),
	('Silk','Silk'),
	('Cotton','Cotton'),
	('Hemp','Hemp'),
	('Dhaka','Dhaka'),
	('Metal Craft','Metal Craft'),
	('Wood Craft','Wood Craft'),
	('Stone Craft','Stone Craft'),
	('Paper Product','Paper Product'),
	('Bamboo Product','Bamboo Product'),
	('Thanka','Thanka'),
	('Beads Items','Beads Items'),
	('Ceramics Products','Ceramics Products'),
	)

class Product(models.Model):
	name=models.CharField(max_length=50)
	image=models.ImageField(upload_to='media/Product Photos')
	price=models.IntegerField()
	description=models.TextField(max_length=500)
	quantity=models.CharField(max_length=50)
	catagories=models.CharField(max_length=50,choices=TYPES)

	def __str__(self):
		return self.name


# Create your models here.
