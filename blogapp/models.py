from django.db import models
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    joined_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Authors"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return (self.name)


class Blog(models.Model):
    admin_author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    author = models.CharField(max_length=150, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog-img/', blank=True, null=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
