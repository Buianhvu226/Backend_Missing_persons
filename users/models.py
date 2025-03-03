import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now
from .enums import *

class User(AbstractUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True, null=False)  # Remove null=True
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="users_groups",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="users_permissions",
        related_query_name="user",
    )

    # def __str__(self):
    #     return str(self.user_id)

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = str(self.user_id)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

class Profile(models.Model):
    profile_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(
        User, 
        to_field='user_id',
        related_name='profiles',
        on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    is_user = models.BooleanField(default=False)
    age = models.PositiveIntegerField(null=True, blank=True)
    city = models.CharField(max_length=50, blank=True)
    district = models.CharField(max_length=50, blank=True)
    ward = models.CharField(max_length=50, blank=True)
    street_address = models.CharField(max_length=255, blank=True)
    gender = models.CharField(
        choices=Gender.choices, max_length=50, blank=True, null=True
    )
    face_image_url = models.URLField(max_length=500, null=True, blank=True)
    name_of_family_members = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(default=now)
    last_active = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    # def __str__(self):
    #     return str(self.profile_id)

class UnknowProfile(models.Model):
    unknown_profile_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    city = models.CharField(max_length=50, blank=True)
    district = models.CharField(max_length=50, blank=True)
    ward = models.CharField(max_length=50, blank=True)
    street_address = models.CharField(max_length=255, blank=True)
    name_of_family_members = models.JSONField(null=True, blank=True)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

    
class Relationship(models.Model):
    relationship_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile_id_1 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_1')
    profile_id_2 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_2')
    relationship = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.profile_id_1} - {self.profile_id_2}"
    
class UserLocation(models.Model):
    location_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    location_lat = models.FloatField(null=True, blank=True)
    location_lon = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.user_id} - {self.location_lat}, {self.location_lon}"

    
