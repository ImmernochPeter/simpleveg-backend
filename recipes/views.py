# pylint:disable=too-many-ancestors
"""
ViewSets für die Recipe API.
"""

from rest_framework.viewsets import ReadOnlyModelViewSet  # type: ignore

from recipes.models import Ingredient, Recipe
from recipes.serializers import (
    IngredientSerializer,
    RecipeDetailSerializer,
    RecipeListSerializer,
)


class RecipeViewSet(ReadOnlyModelViewSet):
    """
    ViewSet für Rezepte.

    list: Alle Rezepte anzeigen
    retrieve: Einzelnes Rezept mit Zutaten anzeigen
    """

    # pylint: disable=no-member
    queryset = Recipe.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return RecipeListSerializer
        return RecipeDetailSerializer


class IngredientViewSet(ReadOnlyModelViewSet):
    """
    ViewSet für Zutaten.
    """

    # pylint: disable=no-member
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
