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

    def __init__(self, name, cook_lvl, cook_time, ingr, descr, reci_t):
        """Class recipe"""
        if type(name) != str or name == "" or type(descr) != str:
            self.error_mess("error : descr and name have to be String but "
                            + type(name) + ", " + type(descr)
                            + " found or name is inexistant")
        else:
            self.name = name
            self.descr = descr

        if type(cook_lvl) != int or type(cook_time) != int or cook_time == "":
            self.error_mess("error : cooking_lvl and cooking_time have \
to be int but " + type(cook_lvl) + ", " + cook_time + " found")
        else:
            if cook_lvl < 1 or cook_lvl > 5:
                self.error_mess("error : cooking_lvl as to be between 1 and 5")
            elif cook_lvl < 0:
                self.error_mess("error : cooking_time can't be neative")
            else:
                self.cook_lvl = cook_lvl
                self.cook_time = cook_time

        if type(ingr) != list:
            self.error_mess("error : ingredients type expected is list but "
                            + type(ingr) + " found")
        else:
            self.ingr = ingr

        if reci_t != "starter" and reci_t != "lunch" and reci_t != "dessert":
            self.error_mess("Recipe type as to be one of starter,\
lunch or dessert")
        else:
            self.reci_t = reci_t

    def __str__(self):
        tot = "  .-.     .-.     .-.     .-.     .-.     .-.     .\
-.     .-.     .-. \n"
        tot += ".'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'\
   `._.'   `._.'   `.\n"
        tot += "{: >37s}".format(self.name)
        tot += "\n  .-.     .-.     .-.     .-.     .-.     .-.   \
  .-.     .-.     .-. \n"
        tot += ".'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'\
   `._.'   `._.'   `.\n"
        tot += "\n\nRecipe type : " + self.reci_t
        tot += "\nCooking level : " + str(self.cook_lvl) + "/5\nCooking\
 time : " + str(self.cook_time) + "min\n\n"
        tot += "List of ingredients:\n"
        for ig in self.ingr:
            tot += "- " + ig + "\n"
        tot += "\nDesciption recipe : " + self.descr + "\n\n"
        return tot
