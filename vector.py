from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        """
        Strings representations
        """
        return 'Vector(%r, %r)" % (self.x, self.y)'

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    # def __bool__(self):
    #     return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


# Soma de vetores
v1 = Vector(2, 4)
v2 = Vector(2, 1)
print("Sum vectors v1 e v2: ", v1 + v2)

# Magnitude de um vetor, utilizando abs.
v = Vector(3, 4)
print("Magnitude de um vetor: ", abs(v))

# Multiplicação de vetores por escalar
v * 3
Vector(9, 12)
print("Multiple vetor v by 3: ", abs(v * 3))


test = [1,2,3,4]
for i in test:
    print(i)

