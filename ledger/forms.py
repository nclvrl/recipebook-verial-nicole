from django import forms
from .models import *

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description']

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'