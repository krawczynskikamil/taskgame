from urllib import request
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import *
from .serializers import *

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Profile.objects.all()
        if self.request.user.is_authenticated:
            return Profile.objects.filter(user=self.request.user)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Task.objects.all()
        if self.request.user.is_authenticated:
            profile = Profile.objects.get(user=self.request.user)
            return Task.objects.filter(profile=profile)

    def get_object(self):
        if self.request.user.is_authenticated:
            return Task.objects.get(pk=self.kwargs['pk'])

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            profile = Profile.objects.get(user=self.request.user)
            # serializer.validated_data['profile'] = profile
            task = serializer.save(profile=profile)
            dates = task.recurrence.occurrences()
            for date in dates:
                Occurance.objects.create(task = task, date = date)

    ##TO DO 
    # update occurances instead of delete and create new
    def update(self, serializer):
        if self.request.user.is_authenticated:
            task = serializer.save()
            dates = task.recurrence.occurrences()
            Occurance.objects.filter(task = task.id).delete()
            for date in dates:
                Occurance.objects.create(task = task, date = date)
            serializer.save()

class OccuranceViewSet(viewsets.ModelViewSet):
    queryset = Occurance.objects.all()
    serializer_class = OccuranceSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Occurance.objects.all()
        if self.request.user.is_authenticated:
            profile = Profile.objects.get(user=self.request.user)
            task = Task.objects.filter(profile=profile)
            return Occurance.objects.filter(task__in=task)

    def update(self, serializer):
        if self.request.user.is_superuser:
            return Occurance.objects.all()
        if self.request.user.is_authenticated:
            oc = Occurance.objects.get(pk=self.kwargs['pk'])
            serializer.save()
            if oc.progres != ProgressType.FINISHED.value:
                oc = Occurance.objects.get(pk=self.kwargs['pk'])
                if oc.progres == ProgressType.FINISHED.value:
                    profile = Profile.objects.get(user=self.request.user)
                    profile.points += oc.task.points
                    profile.save()
            else:
                oc = Occurance.objects.get(pk=self.kwargs['pk'])
                if oc.progres != ProgressType.FINISHED.value:
                    profile = Profile.objects.get(user=self.request.user)
                    profile.points -= oc.task.points
                    profile.save()