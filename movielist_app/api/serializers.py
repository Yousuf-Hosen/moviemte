from rest_framework import serializers
from movielist_app.models import Movie
class MovieSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    title=serializers.CharField()
    description=serializers.CharField()
    active=serializers.BooleanField()
    
    def create(self,validate_data):
        return Movie.objects.create(**validate_data)
    
    def update(self,instance,validate_data):
        instance.title=validate_data.get('title',instance.title)
        instance.description=validate_data.get('description',instance.description)
        instance.active=validate_data.get('active',instance.active)
        instance.save()
        return instance
    
