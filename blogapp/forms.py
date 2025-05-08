from django import forms
from .models import Blog, Author, Category


class CreateBlogForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))

    admin_author = forms.ModelChoiceField(
    queryset= Author.objects.all(),
    widget= forms.Select(attrs={'class':'form-control'})

    )


    class Meta:
        model = Blog
        fields = ['admin_author', 'author', 'category', 'title', 'image', 'body']
        widgets = {
            'image': forms.FileInput(attrs={'class':'form-control'}),
        }