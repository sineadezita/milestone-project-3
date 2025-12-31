from .models import CollaborateRequest
from django import forms
from allauth.account.forms import SignupForm

class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Remove aria-describedby to fix validation error
        for field in self.fields.values():
            if 'aria-describedby' in field.widget.attrs:
                del field.widget.attrs['aria-describedby']
