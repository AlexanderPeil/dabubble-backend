from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from dabubble_backend import settings
from user.views import UserViewSet
from rest_framework import routers
from user.views import (
    GuestLoginView, 
    LoggeduserView,
    SignupView,
    LoginView,
    LogoutView,
    DeleteUserView
)


router = routers.DefaultRouter()
router.register(r'user', UserViewSet, basename='user')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('guest-login/', GuestLoginView.as_view(), name='guest-login'),
    path('edit-user/', LoggeduserView.as_view(), name='edit-user'),
    path('delete-user/', DeleteUserView.as_view(), name='delete-user'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/password_reset/', include('django_rest_passwordreset.urls')),
]  + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)



