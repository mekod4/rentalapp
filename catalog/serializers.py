from django.contrib.auth.models import User, Group
from .models import Film, Genre
from rest_framework import serializers

class GenreSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Genre
		fields = ('name',)

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')


class FilmSerializer(serializers.HyperlinkedModelSerializer):
	genre = GenreSerializer(many=True, read_only=True)
	class Meta:
		model = Film
		fields = ('id', 'title', 'summary', 'cost', 'genre', 'status')