from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm
from .models import *

class districtForm(ModelForm):
    class Meta:
        model = districtTable
        fields = ("__all__")
class areaForm(ModelForm):
    class Meta:
        model = AreaTable
        fields = ("__all__")
