from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	points = models.IntegerField(default=0)
	courses_completed = models.IntegerField(default=0)
	courses_unlocked = models.ManyToManyField('courses.course',blank=True ,related_name='unlocked_by')
	def __str__(self):
		return self.user.username
