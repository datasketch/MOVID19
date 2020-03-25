# accounts/urls.py
from django.urls import include, path

from .views import *

from django.views.generic import TemplateView

urlpatterns = [
    path('home', Home, name='home'),
    path('directions/<str:route>/', Directions, name='Directions'),
    path('stops_by_dir/<str:route>/<str:direction>/', Stops_direction, name='Stops_direction'),
    path('stops_ahead/<str:route>/<str:initial_stop>/<str:direction>/', Stops_ahead, name='Stops_ahead'),
    path('services/<str:route>/<str:initial_stop>/<str:direction>/', Services, name='Services'),
    path('save_person_route/', Save_person_route, name='Save_person_route'),
    path('save_person_no_route/', Save_person_no_route, name='Save_person_no_route'),
]