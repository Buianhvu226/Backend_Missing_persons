from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, ProfileViewSet
from reports.views import MissingReportViewSet, DiscoveryReportViewSet, MatchingResultViewSet
# from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'reports', MissingReportViewSet)
router.register(r'discovery_reports', DiscoveryReportViewSet)
router.register(r'matching_results', MatchingResultViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('api/token-auth/', views.obtain_auth_token),  # Optional: keep default token auth
]
