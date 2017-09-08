from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Supplier(models.Model):
	BUSINESS_CHOICES = (
        ('KS', 'Knitting & Stiching'),
        ('HNDCRFTS', 'Handicrafts'),
        ('OD', 'Ornament Designs'),
        ('DCRNTS', 'Decorations'),
        ('WC', 'Wood Carving'),
        ('AH', 'Animal Husbandary'),
        ('SS', 'Statue Sculpture'),
        ('MD', 'Mask & Dolls'),

    )
	name = models.CharField(max_length=50)
	organization = models.CharField(max_length=50, blank = True)
	location = models.CharField(max_length=30)
	contact = models.CharField(max_length=50)
	business_type = models.CharField(max_length=100, choices = BUSINESS_CHOICES)
	product_name = models.CharField(max_length=50)
	product_price = models.CharField(max_length=50)
	product_image = models.ImageField(upload_to = 'Product Photos')
	publish = models.BooleanField(default=False)

	def __str__(self):
		return 'Supplier Name: {}, Product name : {}'.format(self.name,self.product_name)
