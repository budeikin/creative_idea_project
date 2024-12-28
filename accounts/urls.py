from django.urls import path, include
from . import views

urlpatterns = [
    path('api/', include('accounts.api.urls')),
    path("", include("django.contrib.auth.urls")),
]
