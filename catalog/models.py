from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Genre(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Film(models.Model):

	LOAN_STATUS = (
		('a', 'avaliable'),
		('r', 'rented')
	)

	title = models.CharField(max_length=200)
	summary = models.TextField()
	cost = models.PositiveIntegerField(default=0)
	due_back = models.DateTimeField(null=True, blank=True)
	borrower = models.ForeignKey(User, null=True, blank=True)
	borrower_sid = models.CharField(max_length=7, validators=[RegexValidator(regex='/^([A-Za-z])([0-9]{6})$/', message='SID length has to be 7', code='nomatch')], blank=True)
	status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='a')
	genre = models.ManyToManyField(Genre, help_text='Select a genre for the film', blank=True)

	def __str__(self):
		return self.title