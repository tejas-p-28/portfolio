# pages/admin.py
from django.contrib import admin
from .models import HomePageContent, Resume, ContactSubmission, Education, Project

class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    list_filter = ( 'submitted_at',)
    search_fields = ('name', 'email', 'details')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'description', 'tech_stack')

admin.site.register(HomePageContent)
admin.site.register(Resume)
admin.site.register(ContactSubmission, ContactSubmissionAdmin)
admin.site.register(Education)
admin.site.register(Project, ProjectAdmin)