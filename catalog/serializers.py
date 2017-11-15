import importlib
module = importlib.import_module('.serializers', 'auth-api')
from django.contrib.auth.models import User, Group

from rest_framework import serializers, status, views
from rest_framework.response import Response

from .models import Film, Genre


class GenreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Genre
		fields = ('name',)

class FilmSerializer(serializers.ModelSerializer):
	genre = GenreSerializer(many=True, read_only=True)
	class Meta:
		model = Film
		fields = ('id', 'title', 'summary', 'cost', 'genre', 'status', 'due_back', 'borrower')