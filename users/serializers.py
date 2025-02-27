from rest_framework import serializers
from .models import User, Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    def delete(self, instance):
        return super().delete(instance)
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["user_id", "first_name", "last_name", "age", "city", "district", "ward", "street_address", "gender", "face_image_url", "name_of_family_members", "created_at", "last_active"]
        extra_kwargs = {
            "created_at": {"read_only": True},
            "last_active": {"read_only": True}
        }

    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    def delete(self, instance):
        return super().delete(instance)
    
class RelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["profile_id_1", "profile_id_2", "relationship", "status", "created_at"]
        extra_kwargs = {
            "created_at": {"read_only": True}
        }

    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    def delete(self, instance):
        return super().delete(instance)
    
class UserLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["user_id", "location_lat", "location_lon", "created_at"]
        extra_kwargs = {
            "created_at": {"read_only": True}
        }

    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    def delete(self, instance):
        return super().delete(instance)
    
# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)
    
    
    
