from django.urls import path
from . import views

urlpatterns = [
    # path('all/', views.blog_index, name="all"),
    path('all/', views.BlogIndex.as_view(), name="all"),
    path('read/<int:blog_id>', views.blog_detail, name="blog-detail"),
    path('create_blog/', views.create_blog, name="create-blog"),
    path('update/<int:blog_id>', views.update_blog, name="update-blog"),
    path('delete/<int:blog_id>', views.delete_blog, name="delete-blog")
    

]
