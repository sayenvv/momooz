from django.forms import ModelForm
from .models import *

class districtForm(ModelForm):
    class Meta:
        model = districtTable
        fields = ("__all__")

