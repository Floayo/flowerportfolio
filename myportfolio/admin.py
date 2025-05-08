from django.contrib import admin
from .models import MyInfo, Service, ProjectCategory, Project, PortfolioDetails, ProjectPortfolio

# Register your models here.

admin.site.register(MyInfo)

admin.site.register(ProjectCategory)
admin.site.register(Project)
admin.site.register(PortfolioDetails)
admin.site.register(ProjectPortfolio)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["service_name", "brief_description"]

    