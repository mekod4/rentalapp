from django.db import models


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
	due_back = models.DateField(null=True, blank=True)
	status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='a')
	genre = models.ManyToManyField(Genre, help_text='Select a genre for the film')

	def __str__(self):
		return self.title

