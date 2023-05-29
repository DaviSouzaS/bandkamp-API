from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from .serializers import SongSerializer
from rest_framework.generics import ListCreateAPIView


class SongView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        album_id=self.kwargs.get(self.lookup_field)
        return Song.objects.filter(album_id=album_id)

    serializer_class = SongSerializer

    def perform_create(self, serializer):
        album_id=self.kwargs.get(self.lookup_field)
        return serializer.save(album_id=album_id)
