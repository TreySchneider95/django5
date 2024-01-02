from django.urls import path
from counter import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_two', views.add_2, name='add_2'),
    path('reset', views.reset, name='reset')
]