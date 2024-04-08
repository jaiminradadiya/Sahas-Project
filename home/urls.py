from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

from . import views

urlpatterns = [
  path(''       , views.index,  name='index'),
  path('tables/', views.tables, name='tables'),
  path('demo/',views.demo, name='demo'),

]
