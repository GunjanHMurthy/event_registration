from django.urls import path
from .views import EventListView, EventCreateView, EventDeleteView

urlpatterns = [
    path('events/', EventListView.as_view(), name='event-list'),
    path('events/add/', EventCreateView.as_view(), name='event-add'),
    path('events/delete/<int:pk>/', EventDeleteView.as_view(), name='event-delete'),
]

