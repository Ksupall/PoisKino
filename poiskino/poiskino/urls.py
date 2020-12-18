"""poiskino URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.conf import settings

from app import views as user_views
from app import views
#from app.views import ActorListView #, SearchResultsView, 
'''
path('actor/', views.ActorListView.as_view()),
	path('actor/<int:pk>/', views.ActorDetailView.as_view()),
	path('director/', views.DirectorListView.as_view()),
	path('director/<int:pk>/', views.DirectorDetailView.as_view()),
	path('film/', views.FilmListView.as_view()),
	path('film/<int:pk>/', views.FilmDetailView.as_view()),
	path('list/', views.ListListView.as_view()),
	path('list/<int:pk>/', views.ListDetailView.as_view()),
	path('actor/create/', views.ActorCreateView.as_view()),
	path('director/create/', views.DirectorCreateView.as_view()),


	path('actor/', views.actor_list),
	path('actor/<int:pk>/', views.actor_detail),
	path('actor/search/', views.actor_search),
	'''


from .yasg import urlpatterns as doc_urls

urlpatterns = [
	path('admin/', admin.site.urls),
	path('api-auth/', include('rest_framework.urls')),
	path('actor/', views.ActorListView.as_view()),
	path('actor/<int:pk>/', views.ActorDetailView.as_view()),
	path('actor/create/', views.ActorCreateView.as_view()),
	path('director/', views.DirectorListView.as_view()),
	path('director/<int:pk>/', views.DirectorDetailView.as_view()),
	path('director/create/', views.DirectorCreateView.as_view()),
	path('film/', views.FilmListView.as_view()),
	path('film/<int:pk>/', views.FilmDetailView.as_view()),
	path('film/update/<int:pk>/', views.FilmUpdateView.as_view()),
	path('list/', views.ListListView.as_view()),
	path('list/<int:pk>/', views.ListDetailView.as_view()),
]

urlpatterns += doc_urls

