from django.urls import path
from .views import EventListView, EventCreateView, EventDetailView, register_for_event

urlpatterns = [
    path('', EventListView.as_view(), name='events-list'),
    path('create/', EventCreateView.as_view(), name='event-create'),
    path('<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('<int:pk>/register/', register_for_event, name='event-register'),
]