from django.urls import path
from .views import *

urlpatterns = [
    path("recipes/list/", RecipeList.as_view(), name="recipe_list"),
    path("recipe/<int:pk>/", RecipeDetail.as_view(), name="recipe_detail"),
    path("recipe/add/", add_recipe, name="add_recipe"),
    path("recipe/<int:pk>/add_ingredient/", add_ingredient, name="add_ingredient"),
    path("recipe/<int:pk>/add_image/", add_image, name="add_image"),
]

app_name = "ledger"