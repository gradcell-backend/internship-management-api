from django.db import models
from .validators import validate_resume

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ("internship", "Internship"),
        ("full-time", "Full Time"),
    ]

    COMMITMENT_CHOICES = [
        ("full-time", "Full Time"),
        ("part-time", "Part Time"),
    ]

    LOCATION_CHOICES = [
        ("remote", "Remote"),
        ("hybrid", "Hybrid"),
        ("onsite", "OnSite"),
    ]

    
    title = models.CharField(max_length=255)
    track = models.CharField(max_length=100)
    job_type = models.CharField(
        max_length=1000,
        choices=JOB_TYPE_CHOICES,
        blank=True,
    )
    location_type = models.CharField(
        max_length=1000,
        choices=LOCATION_CHOICES,
        blank=True,
    )
    commitment = models.CharField(
        max_length=1000,
        choices=COMMITMENT_CHOICES,
        blank=True,
    )
    date_posted=models.DateTimeField(auto_now_add=True)

    categories = models.ManyToManyField(
        Category,
        related_name="jobs",
        blank=True
    )

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    job = models.ForeignKey(Job, related_name="applications", on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    university = models.CharField(max_length=255)
    graduation_year = models.IntegerField()
    resume = models.FileField(upload_to="resumes/",validators=[validate_resume])
    cover_letter = models.TextField()

    def __str__(self):
        return f"{self.full_name} - {self.job.title}"


class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.subject
