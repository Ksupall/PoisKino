from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import *
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
	try:
		films = Film.objects.filter(year=2020)
	except Film.DoesNotExist:
		raise Http404
	paginator = Paginator(films, 6)
	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)
	return render(request, "news.html", {"films": page})

def about(request):
	return render(request, "about.html", {})

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Аккаунт создан для { username }!')
			return redirect('../login')
	else:
		form = RegisterForm()
	return render(request, 'register.html', {'form': form})

def film_detail(request, film_id):
	try:
		film = Film.objects.get(pk = film_id)
	except Film.DoesNotExist:
		raise Http404
	genre = film.get_genre_display()
	director = film.directors.all()[0]
	actors = film.actors.all()
	if request.user.is_authenticated == True:
		user = request.user
		try:
			saved = List.objects.get(user_id=user)
		except List.DoesNotExist:
			dic = {
				'film': film,
				'genre': genre,
				'saved': False,
				'director': director,
				'actors': actors
				}
			return render(request, "film_detail.html", dic)
		films = saved.films.all()
		if film in films:
			dic = {
			'film': film,
			'genre': genre,
			'saved': True,
			'director': director,
			'actors': actors
			}
		else:
			dic = {
			'film': film,
			'genre': genre,
			'saved': False,
			'director': director,
			'actors': actors
			}
		return render(request, "film_detail.html", dic)
	else:
		dic = {'film': film,
				'genre': genre,
				'director': director,
				'actors': actors}
		return render(request, "film_detail.html", dic)

def search(request):
	return render(request, "search.html", {})

class SearchResultsView(ListView):
	model = Film
	template_name = 'search_results.html'

	def get_queryset(self):
		name = self.request.GET['name']
		genre = self.request.GET.get('genre')
		country = self.request.GET['country']
		year = self.request.GET.get('year')
		object_list = Film.objects.filter(Q(name__icontains=name))
		if genre != None:
			object_list = object_list.filter(Q(genre__iexact=genre))
		object_list = object_list.filter(Q(country__icontains=country))
		object_list = object_list.filter(Q(year__icontains=year))
		return object_list

def saved(request):
	user = request.user
	try:
		saved = List.objects.get(user_id=user)
	except List.DoesNotExist:
		list = List()
		list.create(user)
		return render(request, "saved.html", {})
	except saved == None:
		return render(request, "saved.html", {})
	object_list = saved.films.all()
	paginator = Paginator(object_list, 6)
	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)
	return render(request, "saved.html", {"object_list": page} )


def saved2(request, film_id):
	if request.method == 'POST':
		action = request.POST.get('change')
		film = Film.objects.get(pk=film_id)
		user = request.user
		saved = List.objects.get(user_id=user)
		if action == "Добавить":
			saved.addtolist(film_id)
		elif action == "Удалить":
			saved.deletefromlist(film_id)

	object_list = saved.films.all()
	paginator = Paginator(object_list, 6)
	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)
	user = request.user
	try:
		saved = List.objects.get(user_id=user)
	except List.DoesNotExist:
		list = List()
		list.create(user)
		return render(request, "saved.html", {"object_list": page})
	except saved == None:
		return render(request, "saved.html", {"object_list": page})
	return render(request, "saved.html", {"object_list": page})