"""
Docstring für recipies.models
"""

from django.db.models import (
    CASCADE,
    CharField,
    ForeignKey,
    ImageField,
    ManyToManyField,
    Model,
    TextField,
    URLField,
)

# Create your models here.


class Ingredient(Model):
    """
    Zutat mit Name und optionalem Link
    """

    name: CharField = CharField(max_length=200)
    link: URLField = URLField(blank=True, null=True)

    # pylint: disable=invalid-str-returned
    def __str__(self):
        return self.name


class Recipe(Model):
    """
    Docstring für Recipe
    """

    title: CharField = CharField(max_length=200)
    description: TextField = TextField()
    ingredients: ManyToManyField = ManyToManyField(
        Ingredient,
        through="RecipeIngredient",
        related_name="recipes",
    )
    instructions: TextField = TextField()
    image: ImageField = ImageField(upload_to="recipes/", blank=True, null=True)


class RecipeIngredient(Model):
    """
    Zwischentabelle für Rezept-Zutaten mit Mengenangabe
    """

    recipe: ForeignKey = ForeignKey(Recipe, on_delete=CASCADE)
    ingredient: ForeignKey = ForeignKey(Ingredient, on_delete=CASCADE)
    amount: CharField = CharField(max_length=100)

    # pylint: disable=too-few-public-methods
    class Meta:
        """
        Docstring für Meta
        """

        unique_together = ["recipe", "ingredient"]

    def __str__(self):
        return f"{self.amount} {self.ingredient.name}"
