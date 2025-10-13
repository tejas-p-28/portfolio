# pages/models.py
from django.db import models

class HomePageContent(models.Model):
    title = models.CharField(max_length=200, default="Building the Future, One Line at a Time")
    subtitle = models.TextField(default="Creative Technologist from India...")
    hero_image = models.ImageField(upload_to='hero_images/')

    def __str__(self):
        return "Homepage Content"

class Resume(models.Model):
    """
    Model to store the uploaded resume file.
    """
    resume_file = models.FileField(upload_to='resumes/', help_text="Upload your latest resume in PDF format.")
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Resume updated on {self.last_updated.strftime('%Y-%m-%d')}"

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    details = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission from {self.name} on {self.submitted_at.strftime('%Y-%m-%d')}"

class Education(models.Model):
    degree = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    start_year = models.CharField(max_length=4)
    end_year = models.CharField(max_length=4)
    description = models.TextField(blank=True, null=True, help_text="Optional: Add details like honors, relevant coursework, etc.")
    order = models.PositiveIntegerField(default=0, help_text="Order to display (e.g., 1 for first, 2 for second)")

    class Meta:
        ordering = ['order'] # Order entries by the 'order' field

    def __str__(self):
        return f"{self.degree} from {self.institution}"