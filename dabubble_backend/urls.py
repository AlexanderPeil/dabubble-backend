from django.contrib import admin
from django.urls import path
from user.views import UserViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'user', UserViewSet, basename='user')


urlpatterns = [
    path('admin/', admin.site.urls),
]
