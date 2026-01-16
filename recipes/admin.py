from django.contrib import admin

from recipes.models import Ingredient, Recipe, RecipeIngredient


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """
    Admin-Interface für Zutaten.
    """

    list_display = ("id", "name", "link")
    search_fields = ("name",)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """
    Admin-Interface für Rezepte.
    """

    list_display = ("id", "title", "description")
    search_fields = ("title",)


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    """
    Admin-Interface für Rezept-Zutaten.
    """

    list_display = ("id", "recipe", "ingredient", "amount")
    search_fields = ("recipe__title", "ingredient__name")
