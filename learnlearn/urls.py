from django.urls import path
from .views import index_view
from . import views

# app_name = 'learnlearn'

urlpatterns = [
    path('', index_view, name='index'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
]
