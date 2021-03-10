from django import forms
from .models import Covid

class CovidForm(forms.ModelForm):
    class Meta:
        model = Covid
        fields = [
            'state'
		] 