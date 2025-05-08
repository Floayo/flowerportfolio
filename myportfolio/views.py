from django.shortcuts import render, get_object_or_404, redirect
from .models import MyInfo, Service, ProjectCategory, Project, PortfolioDetails, ProjectPortfolio
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


def contact_form(request):
    # let's get all user input
    if request.method == "POST":
        print("Post Method in Use!")
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        print(f"{name} sent {message} ")

        # send message
        context = {
            "name": name,
            "email": email,
            "subject": subject,
            "message": message,
        }

    from django.template.loader import render_to_string
    html_text = render_to_string('client_email.html', context)

    from django.core.mail import send_mail
    from django.conf import settings

    send_mail(
        subject=subject,
        # message = f"{name} - {email} - {message}",
        message = None,
        html_message= html_text,
        from_email= settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_HOST_USER],
        fail_silently=False, #True is default

    )

    return redirect('index')