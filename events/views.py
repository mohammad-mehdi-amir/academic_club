from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Event, EventRegistration
from .serializers import EventSerializer, EventCreateSerializer, EventRegistrationSerializer
from accounts.permissions import IsMemberOrAdmin, IsAdmin

class EventListView(generics.ListAPIView):
    queryset = Event.objects.all().order_by('date')
    serializer_class = EventSerializer
    permission_classes = (permissions.AllowAny,)

class EventCreateView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventCreateSerializer
    permission_classes = (IsMemberOrAdmin,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class EventDetailView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.AllowAny,)

from rest_framework.decorators import api_view, permission_classes
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def register_for_event(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if event.registrations.count() >= event.capacity:
        return Response({'detail':'Event is full'}, status=status.HTTP_400_BAD_REQUEST)
    registration, created = EventRegistration.objects.get_or_create(user=request.user, event=event)
    if not created:
        return Response({'detail':'Already registered'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(EventRegistrationSerializer(registration).data, status=status.HTTP_201_CREATED)