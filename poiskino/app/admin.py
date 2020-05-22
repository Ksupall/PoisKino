from django.contrib import admin
from app.models import User, Actor, Director, List, Film, Like

admin.site.register([User, Actor, Director, List, Film, Like])
