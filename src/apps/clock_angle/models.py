import uuid

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class ClockAngle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    hours = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=[MaxValueValidator(24), MinValueValidator(0)],
    )
    minutes = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=[MaxValueValidator(59), MinValueValidator(0)],
    )
    angle = models.PositiveIntegerField(null=False, blank=False)
