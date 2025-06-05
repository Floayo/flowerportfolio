from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404, redirect
from .models import MyInfo, Service, ProjectCategory, Project, PortfolioDetails, ProjectPortfolio, ContactFormLog
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.utils import timezone

# Create your views here.

def home(request):
    # get data from db
    info = MyInfo.objects.first()
    services = Service.objects.all()

    # Portfolio section
    project_category = ProjectCategory.objects.all()

    projects = ProjectPortfolio.objects.all()

    # Portfolio details
    # portfolio_details = PortfolioDetails.objects.all()

    context = {
        'name':info.name,
        'myimage': info.my_image,
        'title1':info.title1,
        'title2':info.title2,
        'phoneno': info.phoneno,
        'location': info.location,
        'birthday': info.birthday,
        'email': info.email,
        'x_handle': info.x_handle,
        'facebook': info.facebook,
        'instagram': info.instagram,
        'linkedin': info.linkedIn,
        'about': info.about,

        # Service
        "services": services,   

        # Project Category
        "project_category":project_category,
        "projects":projects,

        # Portfolio details
        # "portfolio_details":portfolio_details

    }
    return render(request, "index.html", context)

def service_details(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    services = Service.objects.all()
    context = {
        "service":service,
        "services": services
    }
    return render(request, "service-details.html", context)


def portfolio_details(request, portfolio_id):
    # Portfolio details
    portfolio_detail = get_object_or_404(ProjectPortfolio, id=portfolio_id)
    portfolio_details = ProjectPortfolio.objects.all()
    
    context = {
    #    "portfolio_detail": portfolio_detail,
       "portfolio_detail": portfolio_detail,

    }
    return render(request, "portfolio-details.html", context)


# def contact_form(request):
#     # let's get all user input
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
#     #console print
#         print(f"Contact Form message from {name} \n email: {email} \n subject: {subject} \n message:{message}")

#     return redirect('')

from django.http import HttpResponseNotAllowed, JsonResponse
from .models import ContactFormLog  # Ensure this is imported correctly

def contact_form(request):
        if request.method == "POST":
            # print("Post Method in Use!")
            
            # Get user input
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            print(f"{name} sent {message}")

            # Email context
            context = {
                "name": name,
                "email": email,
                "subject": subject,
                "message": message,
            }

            html_context = render_to_string('email.html', context)

            # Set status flags
            is_success = False
            is_error = False
            error_message = ""

            # Try sending mail
            try:
                send_mail(
                    subject=subject,
                    message=None,  # Using HTML message instead
                    html_message=html_context,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
            except Exception as e:
                is_error = True
                error_message = str(e)
                print("Email failed:", error_message)
                messages.error(request, "There was an error. Could not send email.")
                # return JsonResponse({'success': False, 'message': str(e)})

            else:
                is_success = True
                print("Email sent successfully.")
                messages.success(request, "Email has been sent successfully!")
                # return JsonResponse({'success': True})

                # Save to ContactFormLog
            ContactFormLog.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
                sent_time=timezone.now(),
                is_success=is_success,
                is_error=is_error,
                error_message=error_message,
            )

            return redirect('home')  # Update with the correct name of your homepage route
 

    # If not POST, return a method-not-allowed response
# return HttpResponseNotAllowed(['POST'])


