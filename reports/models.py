import uuid
from django.db import models
from django.utils.timezone import now
from users.models import *
from users.enums import *

class MissingReport(models.Model):
    missing_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, to_field='user_id', on_delete=models.CASCADE)
    profile_id = models.ForeignKey(Profile, to_field='profile_id', on_delete=models.CASCADE)
    status = models.CharField(
        choices=MissingStatus.choices, max_length=50, default=MissingStatus.MISSING
    )
    lost_time = models.DateTimeField()
    lost_latitude = models.FloatField()
    lost_longitude = models.FloatField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.profile_id} - {self.status}"
    
class DiscoveryReport(models.Model):
    discovery_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, to_field='user_id', on_delete=models.CASCADE)
    face_image_url = models.URLField(max_length=500, null=True, blank=True)
    found_time = models.DateTimeField()
    found_latitude = models.FloatField()
    found_longitude = models.FloatField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.missing_id} - {self.found_time}"
    
class Matching_Result(models.Model):
    matching_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    missing_id = models.ForeignKey(MissingReport, to_field='missing_id', on_delete=models.CASCADE)
    discovery_id = models.ForeignKey(DiscoveryReport, to_field='discovery_id', on_delete=models.CASCADE)
    face_score = models.FloatField()
    description_score = models.FloatField()
    status_matching = models.CharField(
        choices=MissingStatus.choices, max_length=50, default=MissingStatus.SEARCHING
    )
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.missing_id} - {self.discovery_id}"
