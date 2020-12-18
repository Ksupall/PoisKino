from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import *
from rest_framework import authentication, permissions, generics
#from django.contrib.auth.models import User
#from .forms import RegisterForm
#from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import TemplateView, ListView
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.views import APIView
from .serializers import *
from .service import get_client_ip, FilmFilter
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view

'''
@api_view(['GET', 'POST', 'DELETE'])
def actor_list(request):
	if request.method == 'GET':
		actors = Actor.objects.all()

		name = request.query_params.get('name', None)
		if name is not None:
			actors = actors.filter(name__icontains=name)

		actor_serializer = ActorListSerializer(actors, many=True)
		return JsonResponse(actor_serializer.data, safe=False)

	elif request.method == 'POST':
		actor_data = JSONParser().parse(request)
		actor_serializer = ActorListSerializer(data=actor_data)
		if actor_serializer.is_valid():
			actor_serializer.save()
			return JsonResponse(actor_serializer.data, status=status.HTTP_201_CREATED) 
		return JsonResponse(actor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		count = Actor.objects.all().delete()
		return JsonResponse({'message': '{} Actors were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def actor_detail(request, pk):
	try: 
		actor = Actor.objects.get(pk=pk) 
	except Actor.DoesNotExist: 
		return JsonResponse({'message': 'Actor does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
	if request.method == 'GET': 
		actor_serializer = ActorListSerializer(actor) 
		return JsonResponse(actor_serializer.data) 
 
	elif request.method == 'PUT': 
		actor_data = JSONParser().parse(request) 
		actor_serializer = ActorListSerializer(actor, data=actor_data) 
		if actor_serializer.is_valid(): 
			actor_serializer.save() 
			return JsonResponse(actor_serializer.data) 
		return JsonResponse(actor_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
	elif request.method == 'DELETE': 
		actor.delete() 
		return JsonResponse({'message': 'Actor was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def actor_search(request):
	if request.method == 'GET': 
		name = request.query_params.get('name', None)
		if name is not None:
			actors = Actor.objects.filter(name__icontains=name)
		actors_serializer = ActorListSerializer(actors, many=True)
		return JsonResponse(actors_serializer.data, safe=False)


'''
class ActorListView(generics.ListAPIView):
	"""Вывод списка актеров"""
	queryset = Actor.objects.all()
	serializer_class = ActorSerializer

class ActorDetailView(APIView):
	"""Вывод информации об актере"""
	def get(self, reques, pk):
		actor = Actor.objects.get(id=pk)
		if actor is not None:
			serializer = ActorSerializer(actor)
			return Response(serializer.data)
		else:
			return Response(status=400)

	def delete(self, request, pk):
		actor = Actor.objects.get(id=pk)
		actor = actor.delete()
		return Response(status=201)

class DirectorListView(generics.ListAPIView):
	"""Вывод списка режиссеров"""
	queryset = Director.objects.all()
	serializer_class = DirectorSerializer

class DirectorDetailView(APIView):
	"""Вывод информации о режиссере"""
	def get(self, reques, pk):
		director = Director.objects.get(id=pk)
		if director is not None:
			serializer = DirectorSerializer(director)
			return Response(serializer.data)
		else:
			return Response(400)

	def delete(self, request, pk):
		director = Director.objects.get(id=pk)
		director = director.delete()
		return Response(status=201)

class FilmListView(generics.ListAPIView):
	"""Вывод списка фильмов"""
	queryset = Film.objects.all()
	serializer_class = FilmSerializer
	filter_backend = (DjangoFilterBackend,)
	filter_class = FilmFilter

class FilmDetailView(APIView):
	"""Вывод информации о фильме"""
	def get(self, reques, pk):
		film = Film.objects.get(id=pk)
		serializer = FilmSerializer(film)
		return Response(serializer.data)

class ListListView(generics.ListAPIView):
	"""Вывод списка избранного"""
	queryset = List.objects.all()
	serializer_class = ListSerializer

class ListDetailView(generics.ListAPIView):
	"""Вывод информации об избранном"""
	def get(self, reques, pk):
		list_ = List.objects.get(id=pk)
		serializer = ListSerializer(list_)
		return Response(serializer.data)

class ActorCreateView(APIView):
	def get_object(self, pk):
		return Actor.objects.get(name=pk)

	"""Добавление актера"""
	def post(self, request):
		serializer = ActorCreateSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(status=201)
		else:
			return Response(status=400)

class DirectorCreateView(APIView):
	"""Добавление режиссера"""
	def post(self, request):
		serializer = DirectorCreateSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(status=201)
		else:
			return Response(status=400)

class FilmUpdateView(APIView):

	def patch(self, request, pk):
		film = Film.objects.get(pk=pk)

		print(request.data)
		serializer = FilmUpdateSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(status=201)
		else:
			return Response(status=400)