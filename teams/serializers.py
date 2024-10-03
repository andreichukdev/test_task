from rest_framework import serializers
from .models import Person, Team

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    def validate_email(self, value):
        if Person.objects.filter(email=value).exists():
            raise serializers.ValidationError("A person with this email already exists.")
        return value
    

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

    def validate_name(self, value):
        if Team.objects.filter(name=value).exists():
            raise serializers.ValidationError("A team with this name already exists.")
        return value