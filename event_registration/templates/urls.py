from django.urls import path
from .views import RegistrationCreateView, RegistrationListView

urlpatterns = [
    path('register/', RegistrationCreateView.as_view(), name='event_register'),
    path('registrations/', RegistrationListView.as_view(), name='registration_list'),
]
