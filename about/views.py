from django.shortcuts import render
from .models import About
from .forms import CollaborateForm

# Create your views here.
def about_fashion_tech(request):
    """
    Renders About page
    """
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS, "We have received your collaboration request. Please allow two working days for our response!")
    
    about = About.objects.first()
    collaborate_form = CollaborateForm()
    
    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form
        },
    )