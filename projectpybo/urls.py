from django.urls import path

from . import views

app_name = 'projectpybo'

urlpatterns = [
    path('', views.main),
    path('example/', views.example, name='example'),
]