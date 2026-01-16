"""
URL-Konfiguration für die Recipe API.
"""

from rest_framework.routers import DefaultRouter  # type: ignore

from recipes.views import IngredientViewSet, RecipeViewSet

router = DefaultRouter()
router.register("recipes", RecipeViewSet, basename="recipe")
router.register("ingredients", IngredientViewSet, basename="ingredient")

urlpatterns = router.urls
