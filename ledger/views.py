from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *

class RecipeList(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipes_list.html"
    redirect_field_name = "accounts/login"

class RecipeDetail(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipe.html"
    redirect_field_name = "accounts/login"

@login_required
def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user.profile
            recipe.save()
            return redirect(f"/recipe/{recipe.pk}/", pk=recipe.pk)
    else:
        recipe_form = RecipeForm()
    return render(request, 'add_recipe.html', {'recipe_form': recipe_form})

@login_required
def add_ingredient(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        ingredient_form = IngredientForm(request.POST)
        recipe_ingredient_form = RecipeIngredientForm(request.POST)
        if 'submit_ingredient' in request.POST and ingredient_form.is_valid():
            ingredient_form.save()
            return redirect(f"/recipe/{recipe.pk}/add_ingredient/", pk=recipe.pk)
        if 'submit_recipeingredient' in request.POST and recipe_ingredient_form.is_valid():
            recipe_ingredient = recipe_ingredient_form.save(commit=False)
            recipe_ingredient.recipe = recipe
            recipe_ingredient.save()
            return redirect(f"/recipe/{recipe.pk}/", pk=recipe.pk)
    else:
        ingredient_form = IngredientForm()
        recipe_ingredient_form = RecipeIngredientForm()
    return render(request, 'add_ingredient.html', {
        'ingredient_form': ingredient_form,
        'recipe_ingredient_form': recipe_ingredient_form,
        'recipe': recipe,
    })

@login_required
def add_image(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk) 
    if request.method == "POST":
        image_form = RecipeImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image = image_form.save(commit=False)
            image.recipe = recipe
            image.save()
            return redirect(f"/recipe/{recipe.pk}/", pk=recipe.pk)   
    else:
        image_form = RecipeImageForm()
    return render(request, "add_image.html", {
        "image_form": image_form,
        "recipe": recipe
    })