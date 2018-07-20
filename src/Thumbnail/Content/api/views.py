from rest_framework import generics
from Content.models import Content
from .serializers import ContentSerializer


class ContentCreateAPIView(generics.CreateAPIView):
    serializer_class = ContentSerializer

    def get_queryset():
        return Content.objects.all()

class ContentUpdateAPIView(generics.UpdateAPIView):
    lookup_field = 'pk'
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
