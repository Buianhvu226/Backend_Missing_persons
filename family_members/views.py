from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import FamilyMember
from .serializers import FamilyMemberSerializer
from missing_persons_backend.utils import upload_face_image
import os
import uuid

class FamilyMemberViewSet(viewsets.ModelViewSet):
    queryset = FamilyMember.objects.all()
    serializer_class = FamilyMemberSerializer

    def create(self, request, *args, **kwargs):
        # Handle file upload
        face_image = request.FILES.get('face_image')
        if face_image:
            # Save temporarily
            temp_path = f"temp_{uuid.uuid4()}{os.path.splitext(face_image.name)[1]}"
            with open(temp_path, 'wb+') as destination:
                for chunk in face_image.chunks():
                    destination.write(chunk)
            
            # Upload to Supabase
            file_name = f"{uuid.uuid4()}{os.path.splitext(face_image.name)[1]}"
            public_url = upload_face_image(temp_path, file_name)
            
            # Clean up temp file
            os.remove(temp_path)
            
            if public_url:
                request.data['face_image_url'] = public_url
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)