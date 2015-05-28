from rest_framework import viewsets
from app.api.serializers import exampleSerializer
from app.models import Item

class ExampleViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = exampleSerializer
    lookup_field = 'name'