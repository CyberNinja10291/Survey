
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('data_app.urls')),
    path('api/', include('data_app.urls')),
]