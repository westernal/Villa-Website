from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/villa/', include('quickstart.urls')),
    path('api/user/', include('User.urls')),
]
