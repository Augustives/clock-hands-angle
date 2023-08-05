from django.urls import re_path

from apps.clock_angle.views import ClockAngleView

urlpatterns = [
    re_path(
        r"(?P<hours>\d+)/(?:(?P<minutes>\d+)/)?$",
        ClockAngleView.as_view(),
        name="clock-angle",
    ),
]
