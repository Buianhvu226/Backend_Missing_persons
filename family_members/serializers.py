from rest_framework import serializers
from .models import FamilyMember

class FamilyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMember
        fields = [
            'member_id',
            'user',
            'full_name',
            'dob',
            'gender',
            'description',
            'relations',
            'face_image_url',
            'is_missing',
            'missing_since',
            'created_at'
        ]
        read_only_fields = ['member_id', 'created_at']

    def validate_relations(self, value):
        """
        Check that relations is a valid JSON object
        """
        if not isinstance(value, dict):
            raise serializers.ValidationError("Relations must be a JSON object")
        return value

    def validate_dob(self, value):
        """
        Check that date of birth is not in the future
        """
        from django.utils import timezone
        if value and value > timezone.now().date():
            raise serializers.ValidationError("Date of birth cannot be in the future")
        return value

    def validate_missing_since(self, value):
        """
        Check that missing_since date is not in the future
        """
        from django.utils import timezone
        if value and value > timezone.now():
            raise serializers.ValidationError("Missing since date cannot be in the future")
        return value