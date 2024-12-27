from django.urls import path
from .views import SiloListView

urlpatterns = [
    path('list/', SiloListView.as_view(), name='silo_list')
]
