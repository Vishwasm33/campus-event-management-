from rest_framework import serializers
from .models import College, Event, Student, Registration, Attendance, Feedback


# -------------------
# College Serializer
# -------------------
class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ['id', 'name']


# -------------------
# Event Serializer
# -------------------
class EventSerializer(serializers.ModelSerializer):
    college = CollegeSerializer(read_only=True)  # display college name
    college_id = serializers.PrimaryKeyRelatedField(
        queryset=College.objects.all(), source='college', write_only=True
    )

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'event_type', 'date', 'college', 'college_id']


# -------------------
# Student Serializer
# -------------------
class StudentSerializer(serializers.ModelSerializer):
    college = CollegeSerializer(read_only=True)  # display college name
    college_id = serializers.PrimaryKeyRelatedField(
        queryset=College.objects.all(), source='college', write_only=True
    )

    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'college', 'college_id']


# -------------------
# Registration Serializer
# -------------------
class RegistrationSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)  # display student name
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), source='student', write_only=True
    )
    event = EventSerializer(read_only=True)  # display event title
    event_id = serializers.PrimaryKeyRelatedField(
        queryset=Event.objects.all(), source='event', write_only=True
    )

    class Meta:
        model = Registration
        fields = ['id', 'student', 'student_id', 'event', 'event_id']


# -------------------
# Attendance Serializer
# -------------------
class AttendanceSerializer(serializers.ModelSerializer):
    registration = RegistrationSerializer(read_only=True)
    registration_id = serializers.PrimaryKeyRelatedField(
        queryset=Registration.objects.all(), source='registration', write_only=True
    )
    attended = serializers.BooleanField()

    class Meta:
        model = Attendance
        fields = ['id', 'registration', 'registration_id', 'attended']

    def create(self, validated_data):
        # Use registration object from registration_id
        registration = validated_data.pop('registration')
        attendance = Attendance.objects.create(registration=registration, **validated_data)
        return attendance


# -------------------
# Feedback Serializer
# -------------------
class FeedbackSerializer(serializers.ModelSerializer):
    registration = RegistrationSerializer(read_only=True)
    registration_id = serializers.PrimaryKeyRelatedField(
        queryset=Registration.objects.all(), source='registration', write_only=True
    )
    rating = serializers.IntegerField()

    class Meta:
        model = Feedback
        fields = ['id', 'registration', 'registration_id', 'rating']

    def create(self, validated_data):
        registration = validated_data.pop('registration')
        feedback = Feedback.objects.create(registration=registration, **validated_data)
        return feedback
