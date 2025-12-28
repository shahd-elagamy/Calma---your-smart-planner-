from django.urls import path
from .views import daily_checkin

urlpatterns = [
    path('checkin/', daily_checkin, name='daily_checkin'),
]
