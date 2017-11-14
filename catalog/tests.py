from django.test import TestCase
from .models import Film

class ModelTestCase(TestCase):

	def setUp(self):
		self.title = 'The Big Lebowski'
		self.summary = 'Some summary for this overrated movie'
		self.cost = 11
		self.status = 'a'
		self.film = Film(title=self.title, summary=self.summary, cost=self.cost, status=self.status)

	def test_model_can_create_a_film(self):
		""" Test the film model can create another film"""
		old_films = Film.objects.count()
		self.film.save()
		new_films = Film.objects.count()
		self.assertNotEqual(old_films, new_films)

	def test_model_can_be_readable_in_the_admin(self):
		""" Test the film can be read in the Admin """
		self.assertEqual(str(self.film), self.title)