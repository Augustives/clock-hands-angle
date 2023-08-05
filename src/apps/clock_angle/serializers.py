from rest_framework import serializers
from apps.clock_angle.models import ClockAngle


class ClockAngleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClockAngle
        fields = "__all__"
