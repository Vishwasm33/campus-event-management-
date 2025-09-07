"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from eventapp.views import (
    index,  # <-- add this
    CollegeViewSet,
    EventViewSet,
    StudentViewSet,
    RegistrationViewSet,
    AttendanceViewSet,
    FeedbackViewSet
)

# Create router and register viewsets
router = routers.DefaultRouter()
router.register(r'colleges', CollegeViewSet)
router.register(r'events', EventViewSet)
router.register(r'students', StudentViewSet)
router.register(r'registrations', RegistrationViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'feedback', FeedbackViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # <-- homepage route
    path('api/', include(router.urls)),  # API endpoints
]

