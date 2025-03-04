from django.db import models
import uuid
from django.utils.timezone import now
from users.models import User


class Notification(models.Model):
    notification_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, to_field='user_id', on_delete=models.CASCADE)
    type_message = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.user_id} - {self.title}"