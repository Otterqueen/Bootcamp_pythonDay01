from book import Book
from recipe import Recipe
from datetime import datetime

ingr = ["ham", "cheese", "miam"]
cake = Recipe("cake", 4, 12, ingr, "lol", "lunch")
cake_au_choc = Recipe("cake au choc", 3, 10, ingr, "lol", "lunch")
salad = Recipe("salad", 3, 10, ingr, "je n'aime pas la salade", "lunch")
pain = Recipe("pain", 3, 10, ingr, "lol", "lunch")
pate = Recipe("pate", 3, 10, ingr, "lol", "lunch")
viande = Recipe("viande", 3, 10, ingr, "lol", "lunch")
recipes_list = {"lunch":[pate, viande], "dessert":[cake, cake_au_choc], "starter":[salad, pain]}


to_print = str(cake)
print(to_print)

book = Book("name", datetime.now(), datetime.now(), recipes_list)

book.get_recipe_by_name("salad")
book.get_recipes_by_types("lunch")



# i = datetime.now()
# if type(i) == datetime:
#     print("oui", type(i))
# else:
#     print("non", type(i))

# print(recipes_list.keys())

# if ("lunch" not in recipes_list.keys()) or ("dessert" not in recipes_list.keys()) or ("starter" not in recipes_list.keys()):
#     print("Non")
# else:
#     print("Vouiiii")

# for key in recipes_list.keys():
#     if (key not in ["lunch", "dessert", "starter"]):
#         print("Non")
#     else:
#         print("Vouiiii")