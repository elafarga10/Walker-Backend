from rest_framework import serializers
from .models import WalkEntry

class WalkEntrySerializer(serializers.ModelSerializer):
    walk_url = serializers.ModelSerializer.serializer_url_field(
        view_name='walk_detail')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = WalkEntry
        fields = ('date', 'distance', 'time', 'weight', 'image_url', 'owner', 'id', 'created_at', 'updated_at', 'walk_url',)