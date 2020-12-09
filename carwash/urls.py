from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from api.views import GoogleLogin
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('rest-auth/google', GoogleLogin.as_view(), name='google_login'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('auth/', obtain_auth_token),
    path('', include('main.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)