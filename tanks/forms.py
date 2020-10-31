from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User, Tank, Fertilizer


class TankForm(forms.ModelForm):
    class Meta:
        model = Tank
        fields = ('owner_id', 'alias', 'gallons')
        exclude = ('owner_id', )


class FertilizerForm(forms.ModelForm):
    class Meta:
        model = Fertilizer
        fields = ('brand', 'type')


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', )
