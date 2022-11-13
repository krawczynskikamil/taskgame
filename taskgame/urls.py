from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from tasks import views

router = routers.DefaultRouter()
router.register('profiles', views.ProfileViewSet)
router.register('tasks', views.TaskViewSet)
router.register('occurances', views.OccuranceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include("django.contrib.auth.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)