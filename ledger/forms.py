from django import forms
from .models import *

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description']

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity']
    
    ingredient = forms.ModelChoiceField(queryset=Ingredient.objects.all())