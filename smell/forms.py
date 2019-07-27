from django import forms
from .models import Smell

class UpdateSmell(forms.ModelForm):

    class Meta:
        model=Smell
        # fields = ['smell']
        exclude = ['updated_datetime']