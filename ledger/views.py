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