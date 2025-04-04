from django.db import models
from django.contrib.auth.models import User
from courses.models import course
# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE )
	points = models.IntegerField(default=0)
	name = models.CharField(max_length=30,editable=False)
	courses_completed = models.IntegerField(default=0)
	courses_unlocked = models.ManyToManyField(course ,blank=True ,related_name='unlocked_by')
	def save(self, *args , **kwargs) :
		self.name = self.user.username
		super().save(*args, **kwargs)
	def __str__(self):
		return self.user.username
