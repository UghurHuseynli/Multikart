from django.urls import path
from core.views import homeview


urlpatterns = [
    path('', homeview, name = 'home')
]
