# pages/admin.py
from django.contrib import admin
from .models import HomePageContent, Resume, ContactSubmission

class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    list_filter = ( 'submitted_at',)
    search_fields = ('name', 'email', 'details')

admin.site.register(HomePageContent)
admin.site.register(Resume)
admin.site.register(ContactSubmission, ContactSubmissionAdmin)