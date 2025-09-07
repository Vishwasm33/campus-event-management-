from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count, Avg, Q
from .models import College, Event, Student, Registration, Attendance, Feedback
from .serializers import (
    CollegeSerializer, EventSerializer, StudentSerializer,
    RegistrationSerializer, AttendanceSerializer, FeedbackSerializer
)

# -------------------
# Homepage view
# -------------------
def index(request):
    return render(request, 'eventapp/index.html')

# -------------------
# College ViewSet
# -------------------
class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer

# -------------------
# Event ViewSet
# -------------------
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @action(detail=False, methods=['get'])
    def registrations_count(self, request):
        events = Event.objects.annotate(total_registrations=Count('registrations'))
        data = [{'event': e.title, 'college': e.college.name, 'total_registrations': e.total_registrations} for e in events]
        return Response(data)

    @action(detail=False, methods=['get'])
    def attendance_percentage(self, request):
        events = Event.objects.annotate(
            total_registrations=Count('registrations'),
            attended_count=Count('registrations__attendance', filter=Q(registrations__attendance__attended=True))
        )
        data = []
        for e in events:
            percentage = 0
            if e.total_registrations > 0:
                percentage = (e.attended_count / e.total_registrations) * 100
            data.append({'event': e.title, 'college': e.college.name, 'attendance_percentage': round(percentage, 2)})
        return Response(data)

    @action(detail=False, methods=['get'])
    def average_feedback(self, request):
        events = Event.objects.annotate(avg_feedback=Avg('registrations__feedback__rating'))
        data = [{'event': e.title, 'college': e.college.name, 'average_feedback': round(e.avg_feedback or 0, 2)} for e in events]
        return Response(data)

    @action(detail=False, methods=['get'])
    def popularity(self, request):
        events = Event.objects.annotate(total_registrations=Count('registrations'))
        data = [{'event': e.title, 'college': e.college.name, 'total_registrations': e.total_registrations} for e in events]
        return Response(data)

# -------------------
# Student ViewSet
# -------------------
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# -------------------
# Registration, Attendance, Feedback
# -------------------
class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
