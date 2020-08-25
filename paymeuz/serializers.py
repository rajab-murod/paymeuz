from rest_framework import serializers


class SubscribeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    method = serializers.CharField()
    params = serializers.JSONField()