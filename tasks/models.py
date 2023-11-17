from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from enum import Enum 
from recurrence.fields import RecurrenceField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)

    def create(self, data):
        user_data = data.pop('user')
        user_data['password'] = make_password(user_data.get('password'))
        user = User.objects.create(**user_data)
        profile = Profile.objects.create(user = user, **data)
        return profile

class TaskTypes(Enum):
    EDUCATION ='Education'
    WORK = 'Work'
    FITNESS = 'Fitness'
    SOCIAL = 'Social'
    HOBBY = 'Hobby'

class Task(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=400, null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    points = models.IntegerField(default = 0)
    type = models.CharField(
        max_length = 20,
        choices = [(tag.value, tag.value) for tag in TaskTypes],
        default = TaskTypes.EDUCATION,
    )
    image = models.ImageField(upload_to = 'images/', default = 'images/indeks.png')
    recurrence = RecurrenceField()
    def __str__(self):
        return str(self.profile) + " " + str(self.name) + " " + str(self.type) + " " + str(self.points)

class ProgressType(Enum):
    NOT_STARTED = 'not started'
    PROGRESS = 'in progress'
    FINISHED = 'finished'

class Occurance(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date = models.DateField()
    progres = models.CharField(
        max_length = 20,
        choices = [(tag.value, tag.value) for tag in ProgressType],
        default = ProgressType.NOT_STARTED,
    )

    def __str__(self):
        return str(self.task) + " " + str(self.date) + " " + str(self.progres)