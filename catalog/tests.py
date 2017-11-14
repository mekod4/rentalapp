from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from rest_framework.test import APIClient
from rest_framework import status

from .models import Film


class ModelTestCase(TestCase):
	"""
	Test for the models
	"""
	def setUp(self):
		self.title = 'The Big Lebowski'
		self.summary = 'Some summary for this overrated movie'
		self.cost = 11
		self.status = 'a'
		self.film = Film(title=self.title, summary=self.summary, cost=self.cost, status=self.status)

	def test_model_can_create_a_film(self):
		old_films = Film.objects.count()
		self.film.save()
		new_films = Film.objects.count()
		self.assertNotEqual(old_films, new_films)

	def test_model_can_be_readable_in_the_admin(self):
		self.assertEqual(str(self.film), self.title)


class ViewTestCase(TestCase):
	"""
	Test for the api views
	"""
	def setUp(self):
		user = User.objects.create(username='testuser')
		self.client = APIClient()
		self.client.force_authenticate(user=user)
		self.film_data ={'title': 'test movie', 'summary': 'summary movie', 'cost': 1, 'status': 'a'}
		self.response = self.client.post(
			'/api/films/',
			self.film_data,
			format='json')

	def test_api_can_create_a_film(self):
		self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

	def test_api_can_get_a_specific_film(self):
		film = Film.objects.get(id=1)
		response = self.client.get(
			'/api/films/',
			kwargs={'pk': film.id}, 
			format='json')

	def test_api_can_update_a_film(self):
		test_film = Film.objects.get()
		new_film = {'title': 'New test title film', 'summary': 'test new summary', 'cost': 1, 'status': 'r'}
		res = self.client.put(
			reverse('film-detail', kwargs={'pk': test_film.id}),
			new_film,
			format='json')
		self.assertEqual(res.status_code, status.HTTP_200_OK)

	def test_api_can_delete_a_film(self):
		test_film = Film.objects.get()
		response = self.client.delete(
			reverse('film-detail', kwargs={'pk': test_film.id}),
			format='json',
			follow=True)
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)