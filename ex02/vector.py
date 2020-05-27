import sys


class Vector():

    def __init__(self, values):
        assert isinstance(values, int) or isinstance(values, range) or \
            isinstance(values, tuple) or \
            all(isinstance(x, float) for x in values), \
            "vector as to be int, list, or list of float"

        if type(values) == list:
            self.values = values
            self.size = len(values)
        if type(values) == int:
            self.values = [float(i) for i in range(0, values)]
            self.size = values
        if type(values) == range:
            self.values = [float(i) for i in values]
            self.size = len(values)
        if type(values) == tuple:
            assert len(values) == 2, "Tuple lenght have to be equal to 2"
            r = range(int(values[0]), int(values[1]))
            self.values = [float(i) for i in r]
            self.size = len(values)

    def verif_is_vect(self, vect2):
        assert isinstance(vect2, int) or isinstance(vect2, Vector),\
                "the second parametre has to be a int or a Vector"
        if isinstance(vect2, int):
            return False
        else:
            assert vect2.size == vect2.size, "vectors as no same size"
            return True

    def __add__(self, vect2):
        """ajoute 2 vecteurs"""
        if self.verif_is_vect(vect2):
            new_list = [float(self.values[i] + vect2.values[i])
                        for i in range(0, self.size)]
        return Vector(new_list)

    def __radd__(self, n):
        if self.verif_is_vect(n):
            new_list = [float(self.values[i] + n.values[i])
                        for i in range(0, self.size)]
        else:
            new_list = [float(self.values[i] + n)
                        for i in range(0, self.size)]
        return Vector(new_list)

    def __sub__(self, vect2):
        """soustrait 2 vecteurs"""
        if self.verif_is_vect(vect2):
            new_list = [float(self.values[i] - vect2.values[i])
                        for i in range(0, self.size)]
        return Vector(new_list)

    def __rsub__(self, n):
        if self.verif_is_vect(n):
            new_list = [float(self.values[i] - n.values[i])
                        for i in range(0, self.size)]
        else:
            new_list = [float(self.values[i] - n)
                        for i in range(0, self.size)]
        return Vector(new_list)

    def __truediv__(self, vect2):
        if self.verif_is_vect(vect2):
            new_list = [float(self.values[i] / vect2.values[i])
                        for i in range(0, self.size)]
        return Vector(new_list)

    def __rtruediv__(self, n):
        assert isinstance(n, int) and n != 0,\
            "can not div by 0"
        if self.verif_is_vect(n):
            new_list = [float(self.values[i] / n.values[i])
                        for i in range(0, self.size)]
        else:
            new_list = [float(self.values[i] / n)
                        for i in range(0, self.size)]
        return Vector(new_list)

    def __mul__(self, vect2):
        if self.verif_is_vect(vect2):
            nb = 0
            for i in range(0, self.size):
                nb += float(self.values[i] * vect2.values[i])
            return nb

    def __rmul__(self, n):
        if self.verif_is_vect(n):
            nb = 0
            for i in range(0, self.size):
                nb += float(self.values[i] * n)
            return nb
        else:
            new_list = [float(self.values[i] * n)
                        for i in range(0, self.size)]
            return Vector(new_list)

    def __str__(self):
        formatted_string = "(Vector : {0})"
        return formatted_string.format(self.values)

    def __repr__(self):
        return {'values': self.values, 'size': self.size}
