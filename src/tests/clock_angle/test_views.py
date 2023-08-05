import pytest
from rest_framework.test import APIClient

from apps.clock_angle.views import ClockAngleView
from apps.clock_angle.models import ClockAngle


@pytest.fixture
def client():
    yield APIClient()


class TestClockAngleView:
    @pytest.mark.parametrize(
        "hours,minutes,angle",
        [
            (6, 30, 15),
            (12, 0, 0),
            (6, 0, 180),
        ],
    )
    def test_can_calculate_angle_between_hour_and_minute_hands(
        self, hours: int, minutes: int, angle: float
    ):
        assert (
            ClockAngleView()._calculate_angle_between_hour_and_minute_hands(
                hours, minutes
            )
            == angle
        )

    @pytest.mark.parametrize(
        "hours,minutes,angle",
        [
            (6, 11, 119),
            (4, 33, 61),
            (9, 57, 43),
        ],
    )
    def test_calculate_angle_between_hour_and_minute_hands_rounds_the_angle(
        self, hours: int, minutes: int, angle: float
    ):
        assert (
            ClockAngleView()._calculate_angle_between_hour_and_minute_hands(
                hours, minutes
            )
            == angle
        )

    @pytest.mark.django_db
    def test_can_calculate_angle_when_passing_only_hours(self, client):
        assert len(ClockAngle.objects.all()) == 0
        client.get("/clock-angle/6/")
        assert len(ClockAngle.objects.all()) == 1

    @pytest.mark.django_db
    def test_retrieves_previous_results_instead_of_creating_new_entrys(self, client):
        client.get("/clock-angle/4/45/")
        assert len(ClockAngle.objects.all()) == 1
        client.get("/clock-angle/4/45/")
        assert len(ClockAngle.objects.all()) == 1
