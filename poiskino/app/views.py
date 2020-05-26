from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import *
from django.contrib import messages
from .forms import RegisterForm, SearchForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import TemplateView, ListView

def index(request):
	try:
		films = Film.objects.filter(year=2020)
	except Film.DoesNotExist:
		raise Http404
	return render(request, "news.html", {"films": films})

def detail(request, film_id):
	try:
		film = Film.objects.get(pk = film_id)
	except Film.DoesNotExist:
		raise Http404
	return render(request, "film.html", {"film": film})

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

def film_detail(request):
	film = Film.objects.get(pk=film.id)
	return render(request, "film_detail.html", {"film": film})

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
		'''
		actor_name = self.request.GET.get('actor')
		if Actor.objects.filter(Q(name__icontains=actor_name)).count() == 0:
			messages.error(request, f'Актер не найден!')
		'''
		if genre != None:
			object_list = Film.objects.filter(Q(name__icontains=name) & Q(genre__iexact=genre) &
				Q(country__icontains=country) & Q(year__iexact=year))
		else:
			object_list = Film.objects.filter(Q(name__icontains=name) & Q(country__icontains=country) &
				Q(year__iexact=year))
		return object_list


def saved(request):
	user = request.user
	try:
		saved = List.objects.get(user_id=user)
	except List.DoesNotExist:
		return render(request, "saved.html", {})
	object_list = saved.films.all()
	return render(request, "saved.html", {"object_list": object_list})