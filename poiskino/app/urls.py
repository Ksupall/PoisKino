from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='user'),
    path('<int:film_id>/', views.detail, name='detail')
]