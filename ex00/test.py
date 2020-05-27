from book import Book
from recipe import Recipe
from datetime import datetime

ingr = ["ham", "cheese", "bread"]
ingr2 = ["flour", "chocolate", "eggs"]
ingr3 = ["flour", "yeast", "water"]
ingr4 = ["pasta", "salsa", "peperoni"]
ingr5 = ["beef", "butter", "pepper"]

cake = Recipe("cake", 4, 12, ingr2, "Chocolate cake with baking", "dessert")
cake_au_choc = Recipe("cake au choc", 3, 10, ingr2,
                      "Chocolate cake without baking", "dessert")
salad = Recipe("salad", 3, 10, ingr, "je n'aime pas la salade", "starter")
pain = Recipe("pain", 5, 120, ingr3, "bread homeamade", "starter")
pate = Recipe("pate", 2, 15, ingr4, "Vera pasta from Italy", "lunch")
viande = Recipe("viande", 4, 45, ingr5, "Real beefsteack with sauce", "lunch")

recipes_list = {"lunch": [pate, viande],
                "dessert": [cake, cake_au_choc], "starter": [salad, pain]}


to_print = str(cake)
print(to_print)

book = Book("name", datetime.now(), datetime.now(), recipes_list)

book.get_recipe_by_name("salad")
book.get_recipe_by_name("salad4")
book.get_recipes_by_types("lunch")
book.get_recipes_by_types("lunch3")
