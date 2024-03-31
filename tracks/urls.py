from django.urls import path

from . import views

app_name = 'tracks'

urlpatterns = [
    path('', views.track_list, name='track_list'),
    path('<int:pk>/', views.track_detail, name='track_detail'),
]
