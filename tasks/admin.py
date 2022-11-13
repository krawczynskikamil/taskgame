from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import *

admin.site.unregister(Group)
#admin.site.unregister(User)
admin.site.register(Profile)
admin.site.register(Task)
admin.site.register(Occurance)
