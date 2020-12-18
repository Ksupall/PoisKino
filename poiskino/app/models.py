from django.db import models
from django.contrib.auth.models import User

class FilmQuerySet(models.QuerySet):
	def new2020(self):
		return self.filter(year=2020)

	def get_film_by_id(self, film_id):
		return self.get(id = film_id)


class ListQuerySet(models.QuerySet):
	def get_list_by_user(self, id):
		return self.get(user_id = id)


class Actor(models.Model):
	name = models.CharField(max_length = 150, unique = True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		print("Actor is saved!")
		super().save(*args, **kwargs)

	class Meta:
		ordering = ['name']

class Director(models.Model):
	name = models.CharField(max_length = 150, unique = True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		print("Director is saved!")
		super().save(*args, **kwargs)

	class Meta:
		ordering = ['name']

class Film(models.Model):
	GENRE = (
	(1, "Боевик"),
	(2, "Вестерн"),
	(3, "Детектив"),
	(4, "Документальный"),
	(5, "Драма"),
	(6, "Комедия"),
	(7, "Мелодрама"),
	(8, "Мультфильм"),
	(9, "Сериал"),
	(10, "Триллер"),
	(11, "Фантастика")
	)
	name = models.CharField(max_length = 100, verbose_name = "название")
	description = models.TextField(verbose_name = "описание")
	country = models.CharField(max_length = 100, verbose_name = "страна")
	year = models.PositiveSmallIntegerField(verbose_name = "год")
	genre = models.IntegerField(choices = GENRE, verbose_name = "жанр")
	actors = models.ManyToManyField(Actor, verbose_name = "актеры")
	directors = models.ManyToManyField(Director, verbose_name = "режессеры")

	objects = FilmQuerySet.as_manager()

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		print("Film is saved!")
		super().save(*args, **kwargs)

	def getactors(self):
		return self.actors

	class Meta:
		ordering = ['name']

class List(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	films = models.ManyToManyField(Film, verbose_name = "фильмы")

	objects = ListQuerySet.as_manager()

	def create(self, username):
		self.user_id = username
		self.save()

	def addtolist(self, film_id):
		self.films.add(film_id)
		self.save()

	def deletefromlist(self, film_id):
		self.films.remove(film_id)
		self.save()

	def save(self, *args, **kwargs):
		print("List is saved!")
		super().save(*args, **kwargs)
