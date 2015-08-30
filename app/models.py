from django.db import models
from django.utils import timezone

class Entry(models.Model):

	CATEGORY_CHOICES = (
		('food','food'),
		('med','medication'),
		('ex','exercise'),
		('con','conditions'),
	)

	datetime = models.DateTimeField(default=timezone.now)
	category = models.CharField(choices=CATEGORY_CHOICES,blank=False,null=False,max_length=4)
	value = models.CharField(max_length=80)
	enterdate = models.DateTimeField(auto_now_add=True)
