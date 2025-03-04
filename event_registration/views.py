from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from .models import Event

class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'
    context_object_name = 'events'

class EventCreateView(CreateView):
    model = Event
    template_name = 'event_form.html'
    fields = ['name', 'date', 'description']
    success_url = reverse_lazy('event-list')

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'event_confirm_delete.html'
    success_url = reverse_lazy('event-list')
