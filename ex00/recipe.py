import sys

class Recipe:
    """Classe définissant une recette caractérisée par :
    - name
    - cooking_lvl  
    - cooking_time 
    - ingredients  
    - description  
    - recipe_type"""

    def error_mess(self, mess):
        print(mess + "\n")
        sys.exit()

    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        """Class recipe"""
        if type(name) != str or name == "" or type(description) != str:
            self.error_mess("error : description and name have to be String but " + type(name) + ", " +  type(description) + " found or name is inexistant")
        else:
            self.name = name
            self.description = description

        if (type(cooking_lvl) != int) or (type(cooking_time) != int or cooking_time == ""):
            self.error_mess("error : cooking_lvl and cooking_time type expected is int.")
        else:
            if cooking_lvl < 1 or cooking_lvl > 5:
                self.error_mess("error : cooking_lvl as to be between 1 and 5")
            elif cooking_lvl < 0:
                self.error_mess("error : cooking_time in minute can't be neative")
            else:
                self.cooking_lvl = cooking_lvl
                self.cooking_time = cooking_time

        if type(ingredients) != list:
             self.error_mess("error : ingredients type expected is list but "+ type(ingredients) +" found")
        else:
            self.ingredients = ingredients

        if recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert" :
            self.error_mess("Recipe type as to be one of starter, lunch or dessert")
        else:
            self.recipe_type = recipe_type

    def  __str__(self):
        tot = "  .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-. \n"
        tot += ".'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `.\n"
        tot += "{: >37s}".format(self.name)
        tot += "\n  .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-. \n"
        tot += ".'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `.\n"
        tot += "\n\nRecipe type : " + self.recipe_type
        tot += "\nCooking level : " + str(self.cooking_lvl) + "/5\nCooking time : " + str(self.cooking_time) + "min\n\n"
        tot += "List of ingredients:\n"
        for ig in self.ingredients:
            tot += "- " + ig + "\n"
        tot += "\nDesciption recipe : " + self.description + "\n\n"
        return tot
