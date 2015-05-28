from rest_framework import serializers
from app.models import Item


class exampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name',)
        # read_only_fields = ('date_joined',)
        # write_only_fields = ('password',)