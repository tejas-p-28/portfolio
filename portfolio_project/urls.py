# portfolio_project/urls.py
from django.contrib import admin
from django.urls import path
from django.conf import settings # New
from django.conf.urls.static import static # New

from pages import views as pages_views # New
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pages_views.home, name='home'), # UPDATED
    path('blogs/', blog_views.post_list, name='blog_list'),
]

# This is for serving user-uploaded files (like your resume and hero image) during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)