from django.db import models

class College(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name  # Shows name instead of object in DRF/admin

class Event(models.Model):
    title = models.CharField(max_length=255)
    event_type = models.CharField(max_length=50)
    date = models.DateField()
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='events')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name

class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='registrations')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} -> {self.event.title}"

class Attendance(models.Model):
    registration = models.OneToOneField(Registration, on_delete=models.CASCADE, related_name='attendance')
    attended = models.BooleanField(default=False)

    def __str__(self):
        return f"Attendance: {self.registration.student.name} for {self.registration.event.title}"

class Feedback(models.Model):
    registration = models.OneToOneField(Registration, on_delete=models.CASCADE, related_name='feedback')
    rating = models.IntegerField(default=0)  # 1-5

    def __str__(self):
        return f"Feedback: {self.registration.student.name} for {self.registration.event.title} - {self.rating}"
