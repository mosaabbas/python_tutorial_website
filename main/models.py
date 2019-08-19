from django.db import models
from datetime import datetime
# Create your models here.

class Tutorial(models.Model):
	tut_title = models.CharField(max_length = 200)
	tut_content = models.TextField()
	tut_published = models.DateTimeField('date published', default=datetime.now())

	def __str__(self):
		return self.tut_title