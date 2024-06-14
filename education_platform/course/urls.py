from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_selection, name='course-selection'),
    path('course-overview/', views.course_overview, name='course-overview'),
]