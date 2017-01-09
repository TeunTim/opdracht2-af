from django import forms
from .models import Tosti

class TostiForm(forms.ModelForm):
    class Meta:
        model = Tosti
        fields=('name', 'rating', 'price', 'bread', 'cheese', 'ham', 'tomato', 'bacon')