from rest_framework import generics, permissions
from .serializers import WalkEntrySerializer
from .models import WalkEntry
# from django.contrib.auth.decorators import login_required

# Create your views here.


# @login_required
class WalkEntryList(generics.ListCreateAPIView):
    queryset = WalkEntry.objects.all()
    serializer_class = WalkEntrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# @login_required
class WalkEntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WalkEntry.objects.all()
    serializer_class = WalkEntrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]