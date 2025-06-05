from django.urls import path
from . import views


urlpatterns = [
    path("",views.home, name="home"),
    path("service-details/<int:service_id>/", views.service_details, name="service_details"),
    path("portfolio-details/<int:portfolio_id>/", views.portfolio_details, name="portfolio_details"),
    path("contact_form/", views.contact_form, name="contact_form"),

]

