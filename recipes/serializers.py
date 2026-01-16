"""
Serializers für die Recipe API.
"""

from rest_framework.serializers import ModelSerializer, SerializerMethodField

from recipes.models import Ingredient, Recipe, RecipeIngredient


class IngredientSerializer(ModelSerializer):
    """
    Serializer für Ingredient Model.
    """

    # pylint: disable=too-few-public-methods
    class Meta:
        """
        Docstring für Meta
        """

        model = Ingredient
        fields = ["id", "name", "link"]


class RecipeIngredientSerializer(ModelSerializer):
    """
    Serializer für RecipeIngredient mit verschachtelter Zutat.
    """

    ingredient = IngredientSerializer(read_only=True)

    # pylint: disable=too-few-public-methods
    class Meta:
        """
        Docstring für Meta
        """

        model = RecipeIngredient
        fields = ["id", "ingredient", "amount"]


class RecipeListSerializer(ModelSerializer):
    """
    Serializer für Rezeptliste (ohne Zutaten für Performance).
    """

    # pylint: disable=too-few-public-methods
    class Meta:
        """
        Docstring für Meta
        """

        model = Recipe
        fields = ["id", "title", "description", "image"]


class RecipeDetailSerializer(ModelSerializer):
    """
    Serializer für Rezeptdetails mit allen Zutaten.
    """

    recipe_ingredients: SerializerMethodField = SerializerMethodField()

    # pylint: disable=too-few-public-methods
    class Meta:
        """
        Docstring für Meta
        """

        model = Recipe
        fields = [
            "id",
            "title",
            "description",
            "instructions",
            "image",
            "recipe_ingredients",
        ]

    def get_recipe_ingredients(self, obj: Recipe) -> list[dict]:
        """Holt alle Zutaten mit Mengenangaben für das Rezept."""
        # pylint: disable=no-member
        recipe_ingredients = RecipeIngredient.objects.filter(
            recipe=obj
        ).select_related("ingredient")
        return RecipeIngredientSerializer(recipe_ingredients, many=True).data
