from django.db import models


class Entry(models.Model):
	diary_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	date = models.DateField()
	text = models.TextField()

	def __str__(self):
		return self.name


from django.db import models

# Create your models here.
