import sys
from datetime import datetime

class Book:

    def error_mess(self, mess):
        print(mess + "\n")
        sys.exit()

    def __init__(self, name, last_update, creation_date, recipes_list):
        if type(name) != str:
            self.error_mess("error : String expected but " + type(name) + " found")
        else:
            self.name = name

        if type(last_update) != datetime or type(creation_date) != datetime:
             self.error_mess("error : creation_date and last_update have to be datetime but " + type(creation_date) + ", " + type(last_update) + " found")
        else:
            self.last_update   = datetime
            self.creation_date = creation_date

        if type(recipes_list) != dict:
            self.error_mess("error : list of recipe expected but " + str(type(recipes_list)) + " found")
        else:
            for key in recipes_list.keys():
                if (key not in ["lunch", "dessert", "starter"]):
                    self.error_mess("error : key in recipe list has to be one of those : lunch, dessert, starter but " + key + " found.")
                else:
                    self.recipes_list = recipes_list

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for key in self.recipes_list.keys():
            for recep in self.recipes_list[key]:
                if recep.name == name:
                    print(str(recep))

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        print("Here the list of the recipe of type " + recipe_type + ":")
        for recep in self.recipes_list[recipe_type]:
            print("- " + str(recep.name))

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        self.recipes_list.update(recipe)
        self.last_update = datetime.now()