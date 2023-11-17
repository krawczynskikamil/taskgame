from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('password','username','email')
        extra_kwargs = {
            'password': {
                'write_only': True, 
                'style': {'input_type': 'password'}
                }
            }

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=False)

    class Meta:
        model = Profile
        fields = ('user','points','url')
        extra_kwargs = {
            'points': {'read_only': True},
        }


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields  = ('name','description','points','type','image','recurrence','url')

class OccuranceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Occurance
        fields  = '__all__'

