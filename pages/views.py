# pages/views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import HomePageContent, Resume
from blog.models import Post

def home(request):
    # Fetch all the content needed for the page
    homepage_content = HomePageContent.objects.first()
    resume = Resume.objects.order_by('-last_updated').first()
    try:
        recent_post = Post.objects.latest('publication_date')
    except Post.DoesNotExist:
        recent_post = None

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            submission = form.save()

            # Send email notification
            subject = f"New Portfolio Inquiry from {submission.name}"
            message = f"""
            You have a new contact form submission:

            Name: {submission.name}
            Email: {submission.email}

            Details:
            {submission.details}
            """
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER, # From email
                [settings.EMAIL_HOST_USER], # To email (send to yourself)
                fail_silently=False,
            )

            return redirect('/?submitted=true#contact') # Redirect to contact section with success message
    else:
        form = ContactForm()

    context = {
        'homepage_content': homepage_content,
        'resume': resume,
        'recent_post': recent_post,
        'form': form
    }
    return render(request, 'index.html', context)