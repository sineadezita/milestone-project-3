from django.shortcuts import render
from .models import About

# Create your views here.
def about_fashion_tech(request):
    """
    Renders About page
    """
    about = About.objects.first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )
