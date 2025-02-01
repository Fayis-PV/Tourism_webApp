from django import forms
from .models import *

# Create all forms here:

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = '__all__'
