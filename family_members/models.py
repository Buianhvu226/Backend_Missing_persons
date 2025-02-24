import uuid
from django.db import models
from django.utils.timezone import now
from users.models import User

class FamilyMember(models.Model):
    member_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    description = models.TextField(blank=True, null=True)
    relations = models.JSONField()  # {"father": "Nguyen Van An", "mother": "Tran Thi B"}
    face_encoding = models.JSONField()  # Lưu vector khuôn mặt dưới dạng list
    is_missing = models.BooleanField(default=False)
    missing_since = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(default=now)
