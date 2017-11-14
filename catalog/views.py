from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from rest_framework import permissions
from .serializers import FilmSerializer, UserSerializer
from .models import Film

class UserViewSet(viewsets.ModelViewSet):
	"""
	API Endpoint that allows users to be viewed or edited
	"""
	permission_classes = (permissions.IsAuthenticated,)
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer


class FilmViewSet(viewsets.ModelViewSet):
	""" 
	API Endpoint that allows users to be viewed or edited
	"""
	permission_classes = (permissions.IsAuthenticated,)
	queryset = Film.objects.all()
	serializer_class = FilmSerializer