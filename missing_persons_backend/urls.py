from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from family_members.views import FamilyMemberViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'family_members', FamilyMemberViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
