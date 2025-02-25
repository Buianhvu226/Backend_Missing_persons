import uuid
from django.db import models
from django.utils.timezone import now
from users.models import User

class FamilyMember(models.Model):
    member_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, to_field='user_id', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    description = models.TextField(blank=True, null=True)
    relations = models.JSONField()  # {"father": "Nguyen Van An", "mother": "Tran Thi B"}
    face_image_url = models.URLField(max_length=500, null=True, blank=True)
    is_missing = models.BooleanField(default=False)
    missing_since = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(default=now)
