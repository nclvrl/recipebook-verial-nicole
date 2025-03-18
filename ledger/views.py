from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *

class RecipeList(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipes_list.html"
    redirect_field_name = "accounts/login"

class RecipeDetail(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipe.html"
    redirect_field_name = "accounts/login"