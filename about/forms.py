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
        
        # Change aria-describedby to match Crispy Forms' generated ID
        if 'password1' in self.fields:
            self.fields['password1'].widget.attrs['aria-describedby'] = 'hint_id_password1'