# blog/models.py
from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(help_text="A short summary of the blog post for the homepage.")
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    link_to_original = models.URLField(max_length=500, help_text="Link to the original post on Dev.to or another site.")
    publication_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-publication_date'] # Most recent first

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # This will be used for the "Read Blog" button
        return self.link_to_original