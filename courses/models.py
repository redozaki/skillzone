from django.db import models
from django.forms import ValidationError
from importlib.resources import read_text
import courses.templates as materials
from datetime import timedelta

# Create your models here.

class types(models.TextChoices) :
	soft = 'soft' 
	hard = 'hard'
class course(models.Model) :
	title = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	price = models.IntegerField(default=0)
	type = models.CharField(max_length=10, choices=types.choices , default=types.soft)
	def clean(self) :
		if self.type == types.soft and self.price != 0 :
			raise ValidationError('Soft courses must be free.')
		if self.type == types.hard and self.price == 0 :
			raise ValidationError('Hard courses must have a price.')
	def save(self, *args, **kwargs):
		self.full_clean()
		super().save()
class lesson(models.Model) :
	course = models.ForeignKey(course, related_name='lessons', on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	duration = models.DurationField(default=timedelta(minutes=30))
	position = models.PositiveIntegerField(default=0)
	content = models.TextField(blank=True)
	class Meta:
		ordering = ['position']
		unique_together = ['course', 'position']
	def save(self, *args, **kwargs) :
		if not self.content :
			try :
				self.content = read_text(materials, f'{self.title}.txt', encoding='utf-8')
			except :
				self.content = f"Content for lesson {self.title} not found."
		super().save()