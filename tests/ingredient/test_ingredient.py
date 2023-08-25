from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501
import pytest


# Req 1
def test_ingredient():
    ingredient = Ingredient("bacon")
    ingredient2 = Ingredient("bacon")
    ingredient3 = Ingredient("queijo provolone")
    ingredient4 = Ingredient("queijo mussarela")

    assert isinstance(ingredient, Ingredient)
    assert ingredient.name == "bacon"

    assert repr(ingredient) == "Ingredient('bacon')"

    assert ingredient == ingredient2
    assert ingredient != ingredient3
    assert hash(ingredient) == hash(ingredient2)
    assert hash(ingredient) != hash(ingredient3)

    expected_restrictions = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}

    assert ingredient4.restrictions == expected_restrictions


if __name__ == "__main__":
    pytest.main()
