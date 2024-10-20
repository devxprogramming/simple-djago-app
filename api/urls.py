from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.get_students, name='student'),
]
