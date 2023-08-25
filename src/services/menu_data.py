from models.dish import Dish
from models.ingredient import Ingredient
import csv


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self.load_menu_from_csv(source_path)

    def load_menu_from_csv(self, source_path: str) -> None:
        dishes = dict()

        with open(source_path, mode="r", newline="") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                dish, price, ingredient, recipe_amount = row

                if dish not in dishes:
                    dishes[dish] = Dish(dish, float(price))

                ingredients = Ingredient(ingredient)
                dishes[dish].add_ingredient_dependency(
                    ingredients, int(recipe_amount)
                )

        return set(dishes.values())
