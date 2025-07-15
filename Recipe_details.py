class Food:
    def __init__(self, recipe, ingredients):
        self.recipe = recipe
        self.ingredients = ingredients

    def show(self):
        print(f"Recipe is {self.recipe}")
        print(f"Ingredients are :{", ".join(self.ingredients)}")

r1 = Food("Pasta",["Tomato", "Sause", "Cheese"])
r1.show()

    