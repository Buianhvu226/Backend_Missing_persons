from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from .serializers import MissingReportSerializer, DiscoveryReportSerializer, MatchingResultSerializer


class MissingReportViewSet(viewsets.ModelViewSet):
    queryset = MissingReport.objects.all()
    serializer_class = MissingReportSerializer
    # Remove authentication requirement
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, 
            status=status.HTTP_201_CREATED, 
            headers=headers
        )
    
class DiscoveryReportViewSet(viewsets.ModelViewSet):
    queryset = DiscoveryReport.objects.all()
    serializer_class = DiscoveryReportSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, 
            status=status.HTTP_201_CREATED, 
            headers=headers
        )
    
class MatchingResultViewSet(viewsets.ModelViewSet):
    queryset = Matching_Result.objects.all()
    serializer_class = MatchingResultSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        missing_report = self.perform_create(serializer)
        
        # Get matching results for this report
        matches = Matching_Result.objects.filter(missing_id=missing_report)
        match_serializer = MatchingResultSerializer(matches, many=True)
        
        headers = self.get_success_headers(serializer.data)
        return Response({
            'report': serializer.data,
            'matches': match_serializer.data
        }, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, 
            status=status.HTTP_200_OK, 
            headers=headers
        )
