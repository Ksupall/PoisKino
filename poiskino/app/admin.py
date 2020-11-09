from django.contrib import admin
from app.models import Actor, Director, List, Film

admin.site.register([Actor, Director, List, Film])
