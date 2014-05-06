from django.db import models

# Create your models here.
#representation of data
class Article(models.Model):
	"""docstring for Article"models.Model"""
	name = models.CharField(max_length=200)
	surname = models.CharField(max_length=200)
	mail = models.CharField(max_length=200)
	comment = models.TextField()

	def __unicode__(self):
		return self.name + ' ' + self.surname