from django.db import models

class User(models.Model):
	login = models.CharField(max_length = 50, unique = True,
		verbose_name = "логин")
	email = models.EmailField(max_length = 40, null = True)
	password = models.CharField(max_length = 60, null = True,
		verbose_name = "пароль")
	
	def __str__(self):
		return self.login

	def save(self, *args, **kwargs):
		print("User is saved!")
		super().save(*args, **kwargs)

class Actor(models.Model):
	name = models.CharField(max_length = 150, unique = True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		print("Actor is saved!")
		super().save(*args, **kwargs)

class Director(models.Model):
	name = models.CharField(max_length = 150, unique = True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		print("Director is saved!")
		super().save(*args, **kwargs)

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
	country = models.CharField(max_length = 100, 
		verbose_name = "страна")
	year = models.PositiveSmallIntegerField(verbose_name = "год")
	genre = models.IntegerField(choices = GENRE, verbose_name = "жанр")
	actors = models.ManyToManyField(Actor, verbose_name = "актеры")
	directors = models.ManyToManyField(Director, 
		verbose_name = "режессеры")

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		print("Film is saved!")
		super().save(*args, **kwargs)

class Like(models.Model):
	user_id = models.ForeignKey(User, on_delete = models.PROTECT)
	film_id = models.ForeignKey(Film, on_delete = models.PROTECT)

	def __str__(self):
		return self.id

	def save(self, *args, **kwargs):
		print("Like is saved!")
		super().save(*args, **kwargs)

class List(models.Model):
	user_id = models.ForeignKey(User, on_delete = models.PROTECT)
	name = models.CharField(max_length = 150, unique = True, 
		verbose_name = "название")
	films = models.ManyToManyField(Film, verbose_name = "фильмы")

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		print("List is saved!")
		super().save(*args, **kwargs)

