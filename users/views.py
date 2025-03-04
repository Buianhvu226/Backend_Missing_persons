from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User, Profile
from .serializers import UserSerializer, ProfileSerializer
# from rest_framework.permissions import IsAuthenticated

# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class BaseUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserViewSet(BaseUserViewSet):
    def create(self, request, *args, **kwargs):
        # Create user first
        user_serializer = self.get_serializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        # Then create profile
        profile_data = request.data.get('profile', {})
        profile_data['user_id'] = user.user_id
        profile_serializer = ProfileSerializer(data=profile_data)
        
        if profile_serializer.is_valid():
            profile_serializer.save()
            response_data = {
                'user': user_serializer.data,
                'profile': profile_serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            # If profile creation fails, delete the user
            user.delete()
            return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def create_profile(self, request, pk=None):
        user = self.get_object()
        
        # Check if profile already exists
        if hasattr(user, 'profile'):
            return Response(
                {'detail': 'Profile already exists for this user'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create new profile
        profile_data = request.data
        profile_data['user_id'] = user.user_id
        serializer = ProfileSerializer(data=profile_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = [IsAuthenticated]  # Add authentication requirement

    # def perform_create(self, serializer):
    #     # Ensure the user is authenticated and use the correct user instance
    #     if not self.request.user.is_authenticated:
    #         raise PermissionError("Authentication required to create a profile")
        
    #     # Get the User instance
    #     try:
    #         user = User.objects.get(user_id=self.request.user.user_id)
    #         serializer.save(user_id=user)
    #     except User.DoesNotExist:
    #         raise ValueError("User not found")

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except (PermissionError, ValueError) as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        
# class CustomAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                          context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.user_id,
#             'email': user.email,
#             'is_staff': user.is_staff
#         })