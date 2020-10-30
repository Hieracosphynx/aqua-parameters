from django import forms
from .models import Tank, Fertilizer


class TankForm(forms.ModelForm):
    class Meta:
        model = Tank
        fields = ('owner_id', 'alias', 'gallons')
        exclude = ('owner_id', )


class FertilizerForm(forms.ModelForm):
    class Meta:
        model = Fertilizer
        fields = ('brand', 'type')
