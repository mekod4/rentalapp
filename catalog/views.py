from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from rest_framework import viewsets, permissions, serializers, status, views
from rest_framework.response import Response

from .serializers import FilmSerializer
from .models import Film

class FilmViewSet(viewsets.ModelViewSet):
	""" 
	API Endpoint that allows users to be viewed or edited
	"""
	permission_classes = (permissions.IsAuthenticated,)
	queryset = Film.objects.all()
	serializer_class = FilmSerializer