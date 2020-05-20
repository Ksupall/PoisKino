from django.contrib import admin
from app.models import User, Actor, Director, List, Film, Like

admin.site.register(User)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(List)
admin.site.register(Film)
admin.site.register(Like)
