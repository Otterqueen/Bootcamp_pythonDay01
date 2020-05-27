import sys
from vector import Vector

try:
    # vec1 = Vector("bonjour") #Erreur
    range1 = range(10, 15)
    vec1 = Vector([0.0, 1.0, 2.0, 3.0])
    vec2 = Vector(3)
    vec3 = Vector((10, 15))
    vec4 = Vector(range1)
    print(vec1.__dict__)
    print(vec2.__dict__)
    print(vec3.__dict__)
    print(vec4.__dict__)
    print(str(vec4))
    vec5 = vec1 - vec3
    v6 = vec3 - vec1
    print(vec5)
    print(v6)
    print(vec2 * 3)
    print(vec2 * vec1)
except AssertionError as err:
    print(err)
