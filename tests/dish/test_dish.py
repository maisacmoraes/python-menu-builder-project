from src.models.dish import Dish, Ingredient  # noqa: F401, E261, E501
import pytest


# Req 2
def test_dish():
    dish = Dish("Lasanha", 15.99)
    dish1 = Dish("Lasanha", 15.99)
    dish2 = Dish("Pizza", 12.5)
    dish3 = Dish("Salad", 5.0)

    assert isinstance(dish, Dish)
    assert dish.name == "Lasanha"
    assert dish.price == 15.99

    with pytest.raises(ValueError):
        Dish("Invalid Dish", -5.0)

    with pytest.raises(TypeError):
        Dish("Invalid Dish", "not a float")

    assert repr(dish2) == "Dish('Pizza', R$12.50)"

    assert dish == dish1

    assert hash(dish) == hash(dish1)
    assert hash(dish) != hash(dish2)

    ingredient = Ingredient("Tomato")
    dish3.add_ingredient_dependency(ingredient, 2)
    assert ingredient in dish3.recipe
    assert dish3.recipe[ingredient] == 2

    dish = Dish("Pasta", 8.0)
    ingredient1 = Ingredient("Tomato")
    ingredient2 = Ingredient("Cheese")
    ingredient3 = Ingredient("Bacon")
    dish.add_ingredient_dependency(ingredient1, 2)
    dish.add_ingredient_dependency(ingredient2, 1)
    dish.add_ingredient_dependency(ingredient3, 1)

    assert dish.get_restrictions() == set(
        [r for i in dish.recipe.keys() for r in i.restrictions]
    )

    dish = Dish("Soup", 6.0)
    ingredient1 = Ingredient("Onion")
    ingredient2 = Ingredient("Carrot")
    ingredient3 = Ingredient("Potato")
    dish.add_ingredient_dependency(ingredient1, 2)
    dish.add_ingredient_dependency(ingredient2, 1)
    dish.add_ingredient_dependency(ingredient3, 1)

    assert dish.get_ingredients() == set(dish.recipe.keys())


if __name__ == "__main__":
    pytest.main()
