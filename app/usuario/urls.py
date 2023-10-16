from django.urls import path

from .views import UserRegisterView, UpdatePasswordView


urlpatterns = [
    path('registro/',UserRegisterView.as_view(),name='registro'),
    path('modicontrasena/',UpdatePasswordView.as_view(),name='modicontrasena'),
]