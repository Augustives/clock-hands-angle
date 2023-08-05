import math

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.clock_angle.models import ClockAngle
from apps.clock_angle.serializers import ClockAngleSerializer


class ClockAngleView(APIView):
    def _get_angle_between_hour_and_minute_hands(
        self, hours: int, minutes: int
    ) -> float:
        """
        Takes in the value of hours and minutes and returns
        the the rounded down smaller angle between the clock hands.

        Args:
            hours (int): int value between 0 and 24
            minutes (int): int value between 0 and 59

        Returns:
            float: angle
        """
        hour_angle = (hours % 12) * 30 + minutes * 0.5
        minute_angle = 6 * minutes

        angle_difference = abs(hour_angle - minute_angle)
        angle = min(angle_difference, 360 - angle_difference)

        return math.floor(angle)

    def get(
        self, request: Request, hours: int, minutes: int = 0, format=None
    ) -> Response:
        serializer = ClockAngleSerializer(
            data={"hours": hours, "minutes": minutes, "angle": 0}
        )

        if serializer.is_valid():
            try:
                clock_angle: ClockAngle = ClockAngle.objects.get(
                    hours=hours, minutes=minutes
                )
                angle = clock_angle.angle

            except ClockAngle.DoesNotExist:
                angle = self._get_angle_between_hour_and_minute_hands(
                    int(hours), int(minutes)
                )
                serializer.validated_data["angle"] = angle
                serializer.save()

            return Response({"angle": angle})
        else:
            return Response(serializer.errors, status=400)
