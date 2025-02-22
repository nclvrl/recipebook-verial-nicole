from django.shortcuts import render

def recipes_list(request):
    ctx = {
        "recipes": [
                {
                    "name": "Recipe 1",
                    "ingredients": [
                        {
                            "name": "tomato",
                            "quantity": "3pcs"
                        },
                        {
                            "name": "onion",
                            "quantity": "1pc"
                        },
                        {
                            "name": "pork",
                            "quantity": "1kg"
                        },
                        {
                            "name": "water",
                            "quantity": "1L"
                        },
                        {
                            "name": "sinigang mix",
                            "quantity": "1 packet"
                        }
                    ],
                    "link": "/recipe/1"
                },
                {
                    "name": "Recipe 2",
                    "ingredients": [
                        {
                            "name": "garlic",
                            "quantity": "1 head"
                        },
                        {
                            "name": "onion",
                            "quantity": "1pc"
                        },
                        {
                            "name": "vinegar",
                            "quantity": "1/2cup"
                        },
                        {
                            "name": "water",
                            "quantity": "1 cup"
                        },
                        {
                            "name": "salt",
                            "quantity": "1 tablespoon"
                        },
                        {
                            "name": "whole black peppers",
                            "quantity": "1 tablespoon"
                        },
                        {
                            "name": "pork",
                            "quantity": "1 kilo"
                        }
                    ],
                    "link": "/recipe/2"
                }
            ]
        }
    return render(request, 'recipes_list.html', ctx)

def recipe(request, num=1):
    if num == 1:
        ctx = {
            "name": "Recipe 1",
            "ingredients": [
                {
                    "name": "tomato",
                    "quantity": "3pcs"
                },
                {
                    "name": "onion",
                    "quantity": "1pc"
                },
                {
                    "name": "pork",
                    "quantity": "1kg"
                },
                {
                    "name": "water",
                    "quantity": "1L"
                },
                {
                    "name": "sinigang mix",
                    "quantity": "1 packet"
                }
            ],
            "link": "/recipe/1"
        }
    elif num == 2:
        ctx = {
        "name": "Recipe 2",
        "ingredients": [
            {
                "name": "garlic",
                "quantity": "1 head"
            },
            {
                "name": "onion",
                "quantity": "1pc"
            },
            {
                "name": "vinegar",
                "quantity": "1/2cup"
            },
            {
                "name": "water",
                "quantity": "1 cup"
            },
            {
                "name": "salt",
                "quantity": "1 tablespoon"
            },
            {
                "name": "whole black peppers",
                "quantity": "1 tablespoon"
            },
            {
                "name": "pork",
                "quantity": "1 kilo"
            }
        ],
        "link": "/recipe/2"
    }
    return render(request, 'recipe.html', {'recipe':ctx})