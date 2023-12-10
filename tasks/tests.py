from django.test import TestCase
from django.contrib.auth.models import User
from .models import *
class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='user',
            password = 'haslo'
        )

        self.profile = Profile.objects.create(user = self.user)


    def test_user_is_created_on_profile_creation(self):
        self.assertEquals(self.profile.user.username, 'user')
    
    def test_profile_has_0_points_on_creation(self):
        self.assertEquals(self.profile.points, 0)

    def test_task_creation(self):
        self.task = Task.objects.create(
            name='ćwiczenia',
            description = 'Kardio',
            profile = self.profile,
            type = TaskTypes.FITNESS,
            recurrence = "RRULE:FREQ=MONTHLY;BYMONTHDAY=1;INTERVAL=3;UNTIL=20230827T000000Z"
        )
        self.assertEquals(self.task.points, 0)


    
    # def test_false(self):
    #     self.assertTrue(False)