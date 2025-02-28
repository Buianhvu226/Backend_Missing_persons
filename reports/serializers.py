from rest_framework import serializers
from .models import MissingReport, DiscoveryReport, Matching_Result

class MissingReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissingReport
        fields = [
            'missing_id', 
            'user_id', 
            'profile_id',
            'status',
            'lost_time',
            'lost_latitude',
            'lost_longitude',
            'description',
            'created_at'
        ]
        read_only_fields = ['missing_id', 'created_at']
        extra_kwargs = {
            'user_id': {'write_only': True},
            'profile_id': {'write_only': True}
        }

    def create(self, validated_data):
        # Create the missing report
        missing_report = super().create(validated_data)
        
        # Get all existing discovery reports
        discovery_reports = DiscoveryReport.objects.all()
        
        # Compare with each discovery report
        for discovery in discovery_reports:
            # Calculate matching scores
            face_score = 0  # Implement your face matching logic here
            description_score = 0  # Implement your text matching logic here
            
            # Create matching result
            Matching_Result.objects.create(
                missing_id=missing_report,
                discovery_id=discovery,
                face_score=face_score,
                description_score=description_score,
                status_matching='PENDING'  # or your default status
            )
        
        return missing_report
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    def delete(self, instance):
        return super().delete(instance)
    
class DiscoveryReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscoveryReport
        fields = [
            'discovery_id',
            'user_id',
            'face_image_url',
            'found_time',
            'found_latitude',
            'found_longitude',
            'description',
            'created_at'
        ]
        read_only_fields = ['discovery_id', 'created_at']
        extra_kwargs = {
            'user_id': {'write_only': True}
        }

    def create(self, validated_data):
        # Create the discovery report
        discovery_report = super().create(validated_data)
        
        # Get all existing missing reports
        missing_reports = MissingReport.objects.all()
        
        # Compare with each missing report
        for missing in missing_reports:
            # Calculate matching scores
            face_score = 0  # Implement your face matching logic here
            description_score = 0  # Implement your text matching logic here
            
            # Create matching result
            Matching_Result.objects.create(
                missing_id=missing,
                discovery_id=discovery_report,
                face_score=face_score,
                description_score=description_score,
                status_matching='PENDING'  # or your default status
            )
        
        return discovery_report
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    def delete(self, instance):
        return super().delete(instance)
    
class MatchingResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matching_Result
        fields = [
            'matching_id',
            'missing_id',
            'discovery_id',
            'face_score',
            'description_score',
            'status_matching',
            'created_at'
        ]
        read_only_fields = ['matching_id', 'created_at']
        extra_kwargs = {
            'missing_id': {'write_only': True},
            'discovery_id': {'write_only': True}
        }

    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    def delete(self, instance):
        return super().delete(instance)
    
