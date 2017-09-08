
from django.contrib import admin

# Register your models here.
from .models import Forum

class ForumAdmin(admin.ModelAdmin):
	list_display=['pk','name']

admin.site.register(Forum)
