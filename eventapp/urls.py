from django.urls import path, include
from rest_framework import routers
from .views import (
    CollegeViewSet, EventViewSet, StudentViewSet,
    RegistrationViewSet, AttendanceViewSet, FeedbackViewSet
)

router = routers.DefaultRouter()
router.register(r'colleges', CollegeViewSet)
router.register(r'events', EventViewSet)
router.register(r'students', StudentViewSet)
router.register(r'registrations', RegistrationViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'feedback', FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),  # All API endpoints under /api/
]
