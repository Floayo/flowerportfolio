from django.db import models

# Create your models here.

class MyInfo(models.Model):
    name = models.CharField(max_length=100)
    my_image = models.ImageField(upload_to='My_img/', blank=True, null=True)
    title1 = models.CharField(max_length= 100)
    title2 = models.CharField(max_length= 100, blank=True, null=True)
    phoneno = models.CharField(max_length=16)
    location = models.CharField(max_length= 20)
    birthday = models.CharField(max_length=20)
    email = models.EmailField(max_length= 50) 
    # Socials
    x_handle = models.URLField(max_length= 100)
    facebook = models.URLField(max_length= 100)
    instagram = models.URLField(max_length= 100)
    linkedIn = models.URLField(max_length= 100)
    about = models.TextField()

    class Meta:
        verbose_name_plural = "MyInfo"

    def __str__(self):
        return (self.name) 
    
from ckeditor.fields import RichTextField

class Service(models.Model):
    icon = models.CharField(max_length=50)
    service_name = models.CharField(max_length=200)
    service_image = models.ImageField(upload_to="service/")
    service_box_description = models.TextField()
    brief_description = models.TextField()
    service_body = RichTextField()


    def __str__(self):
        return self.service_name


# Portfolio/Products
class ProjectCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Portfolio Category: {self.name}"
    
class ProjectPortfolio(models.Model):
    category = models.ForeignKey(ProjectCategory, on_delete=models.PROTECT)
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image1 = models.ImageField(upload_to='details/')
    image2 = models.ImageField(upload_to='details/')
    image3 = models.ImageField(upload_to='details/')
    image4 = models.ImageField(upload_to='details/')
    client = models.CharField(max_length=100)
    project_date = models.CharField(max_length=20)
    project_url = models.URLField(max_length=100)
    project_title = RichTextField()
    project_description = RichTextField()

    class Meta:
        verbose_name_plural = "Portfolio"

    def __str__(self):
        return f"Portfolio Project: {self.project_title}"





# Delete later   
class Project(models.Model):
    category = models.ForeignKey(ProjectCategory, on_delete=models.PROTECT)
    title = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Portfolio Project: {self.title} Category: {self.category}"


class PortfolioDetails(models.Model):
    category = models.ForeignKey(ProjectCategory, on_delete=models.PROTECT)
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200)
    image1 = models.ImageField('details/')
    image2 = models.ImageField('details/')
    image3 = models.ImageField('details/')
    image4 = models.ImageField('details/')
    client = models.CharField(max_length=100)
    project_date = models.CharField(max_length=20)
    project_url = models.URLField(max_length=100)
    project_title = RichTextField()
    project_description = RichTextField()

    class Meta:
        verbose_name_plural = "PortfolioDetails"

    def __str__(self):
        return f"Portfolio Project: {self.project_title}"




class ContactFormLog(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)
    message = models.TextField()
    sent_time = models.DateTimeField(null=True, blank=True)
    is_success = models.BooleanField(default=False)
    is_error = models.BooleanField(default=False)
    error_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}" - {self.email}

