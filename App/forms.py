from django import forms
from App.models import *

class ProfileForm(forms.ModelForm):
    class Meta():
        model=Profile
        fields='__all__'
        label={'pic': 'Picture','address':'Address'}