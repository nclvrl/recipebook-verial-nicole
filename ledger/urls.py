from django.urls import path
from .views import *

urlpatterns = [
    path("recipes/list/", RecipeList.as_view(), name="recipe_list"),
    path("recipe/<int:pk>/", RecipeDetail.as_view(), name="recipe_detail"),
    path("recipe/<int:pk>/add_image/", add_image, name="add_image"),
]

app_name = "ledger"