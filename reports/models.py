import uuid
from django.db import models
from django.utils.timezone import now
from users.models import User
from family_members.models import FamilyMember

class MissingReport(models.Model):
    report_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    location_lat = models.FloatField()
    location_lon = models.FloatField()
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('resolved', 'Resolved')])
    details = models.TextField()
    created_at = models.DateTimeField(default=now)


class SightingReport(models.Model):
    sighting_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reporter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    location_lat = models.FloatField()
    location_lon = models.FloatField()
    photo_url = models.URLField()
    face_encoding = models.JSONField(null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(default=now)
