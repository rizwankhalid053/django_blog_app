from django import forms
from django.contrib.auth.models import User

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField() # Ensures the user types a valid email address structure

    class Meta:
        model = User
        fields = ['username', 'email'] # The exact database columns we want to let them edit