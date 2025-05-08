from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Category, Blog
from .forms import CreateBlogForm
# Create your views here.

def blog_index(request):
    blogs = Blog.objects.all()

    context = {
        "blogs": blogs
    }
    return render(request, "blog/blog-index.html", context)

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {
        'blog':blog
    }
    return render(request, 'blog/read_detail.html', context)

def create_blog(request):
    form = CreateBlogForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('all')
        else:
            print("Form is not valid", form.errors)
            return render(request, "blog/create-blog.html", {"form":form})
    else:
        return render(request, 'blog/create_blog.html', {'form':form})
    

def update_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        form = CreateBlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            print("Form updated")
            return redirect('all')
    else: #Get http request
        form = CreateBlogForm(instance=blog)
        return render(request, "blog/update_blog.html", {"form":form})
    
    
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect('all')
