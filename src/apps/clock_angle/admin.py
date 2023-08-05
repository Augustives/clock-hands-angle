from django.contrib import admin

from apps.clock_angle.models import ClockAngle


class ClockHoursAngleAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "hours", "minutes", "angle")
    search_fields = ("id", "hours", "minutes")
    ordering = ("-created_at", "-hours", "-minutes")


admin.site.register(ClockAngle, ClockHoursAngleAdmin)
