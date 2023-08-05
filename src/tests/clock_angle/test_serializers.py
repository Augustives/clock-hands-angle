import pytest
from rest_framework import serializers

from apps.clock_angle.serializers import ClockAngleSerializer


class TestClockAngleSerializer:
    @pytest.mark.parametrize("hours", [25, 30, 48])
    def test_serializer_raises_validation_error_when_hours_is_greater_than_maximum(
        self, hours: int
    ):
        serializer = ClockAngleSerializer(
            data={"hours": hours, "minutes": 0, "angle": 0}
        )
        with pytest.raises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)

        assert (
            str(serializer.errors["hours"][0])
            == "Ensure this value is less than or equal to 24."
        )

    @pytest.mark.parametrize("hours", [-1, -12, -24])
    def test_serializer_raises_validation_error_when_hours_is_less_than_maximum(
        self, hours: int
    ):
        serializer = ClockAngleSerializer(
            data={"hours": hours, "minutes": 0, "angle": 0}
        )
        with pytest.raises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)

        assert (
            str(serializer.errors["hours"][0])
            == "Ensure this value is greater than or equal to 0."
        )

    @pytest.mark.parametrize("minutes", [60, 70, 120])
    def test_serializer_raises_validation_error_when_minutes_is_greater_than_maximum(
        self, minutes: int
    ):
        serializer = ClockAngleSerializer(
            data={"hours": 0, "minutes": minutes, "angle": 0}
        )
        with pytest.raises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)

        assert (
            str(serializer.errors["minutes"][0])
            == "Ensure this value is less than or equal to 59."
        )

    @pytest.mark.parametrize("minutes", [-1, -59, -60])
    def test_serializer_raises_validation_error_when_minutes_is_greater_than_maximum(
        self, minutes: int
    ):
        serializer = ClockAngleSerializer(
            data={"hours": 0, "minutes": minutes, "angle": 0}
        )
        with pytest.raises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)

        assert (
            str(serializer.errors["minutes"][0])
            == "Ensure this value is greater than or equal to 0."
        )
