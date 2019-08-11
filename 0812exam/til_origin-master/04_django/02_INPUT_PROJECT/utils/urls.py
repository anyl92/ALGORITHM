from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # utils/
    path('art/', views.art),  # utils/art/
    path('output/', views.output),  # utils/output/
]
