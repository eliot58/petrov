from rest_framework import serializers


class BonusSerializer(serializers.Serializer):
    s_code = serializers.CharField(max_length=20)
    date_create = serializers.DateField()
    shape = serializers.CharField(max_length=80)
    implement = serializers.CharField(max_length=80)
    glazing = serializers.CharField(max_length=80)
    shape_m2 = serializers.FloatField()
    implement_amount = serializers.IntegerField()
    glazing_m2 = serializers.FloatField()