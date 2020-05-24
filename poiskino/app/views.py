from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import *
from django.contrib import messages
from .forms import RegisterForm


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
			password = form.cleaned_data.get('password')
			messages.success(request, f'Аккаунт создан для { username }!')
			user = User.objects.create(login = username, password = password)
			user.save()
			return redirect('../login')
	else:
		form = RegisterForm()
	return render(request, 'register.html', {'form': form})

def search(request):
	return render(request, "search.html", {})

def films(request):
	films = Film.objects.all()
	return render(request, "list.html", {"films": films})