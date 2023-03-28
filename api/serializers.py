from rest_framework import serializers


class BonusSerializer(serializers.Serializer):
    s_code = serializers.CharField(max_length=20)
    date_create = serializers.DateField()
    shape = serializers.JSONField()
    implement = serializers.JSONField()
    glazing = serializers.JSONField()