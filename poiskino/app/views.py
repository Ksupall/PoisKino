from django.shortcuts import render
from django.http import HttpResponse, Http404
from app.models import Film, Actor

def index(request):
	#films = Film.objects.filter(year=2020)
	films = Film.objects.all()
	return render(request, "news.html", {"films": films})

def detail(request, film_id):
	try:
		film = Film.objects.get(pk = film_id)
	except Film.DoesNotExist:
		raise Http404
	s = "film.id " + str(film.id) + "<br><br>" +" - film.name" + film.name
	return HttpResponse(s)

def about(request):
	return render(request, "about.html", {})