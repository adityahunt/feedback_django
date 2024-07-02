from django.urls import path
from . import views

urlpatterns = [
    path('feedback/', views.feedback_view, name='feedback_form'),
    path('thanks/', views.feedback_thanks, name='feedback_thanks'),
]
