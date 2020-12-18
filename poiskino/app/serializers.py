from rest_framework import serializers

from .models import *

class ActorSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Actor
		fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Director
		fields = '__all__'

class FilmSerializer(serializers.ModelSerializer):
	actors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
	directors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
	class Meta:
		model = Film
		fields = '__all__'

class ListSerializer(serializers.ModelSerializer):
	films = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
	class Meta:
		model = List
		fields = '__all__'

class ActorCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Actor
		exclude = ()

	def create(self, validated_data):
		actor = Actor.objects.update_or_create(
		name = validated_data.get('name', None)
		)
		return actor

class DirectorCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Director
		exclude = ()
		
	def create(self, validated_data):
		director = Director.objects.update_or_create(
		name = validated_data.get('name', None)
		)
		return director

class FilmUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Film
		exclude = ()

	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		print(instance.name)
		#instance.description = validated_data.get('description', instance.description)
		#instance.body = validated_data.get('body', instance.body)
		#instance.author_id = validated_data.get('author_id', instance.author_id)
		instance.save()
		return instance
