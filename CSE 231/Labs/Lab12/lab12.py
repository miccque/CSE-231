import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return "({:.2f}, {:.2f})".format(float(self.x),float(self.y))

    def __repr__(self):
        return "({:.2f}, {:.2f})".format(float(self.x),float(self.y))

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (int,float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def magnitude(self):
        return round(math.sqrt(self.x**2 + self.y**2), 2)

    def unit(self):
        magnitude = self.magnitude()
        if magnitude == 0:
            raise ValueError("Cannot convert zero vector to a unit vector")
        else:
            return Vector(float(float(self.x) / float(magnitude)), float(float(self.y) / float(magnitude)))

def test():
    v1 = Vector(1, 2)
    v2 = Vector(2, 3)

    print(v1)
    print(v2)

    v_addition = v1 + v2
    print(v_addition)

    v_minus = v1 - v2
    print(v_minus)

    v_mult = v1 * 2
    print(v_mult)

    dot_product = v1 * v2
    print(dot_product)

    scalar_product = 2.5 * v1
    print(scalar_product)

    magnitude_v1 = v1.Magnitude()
    print(magnitude_v1)

    unit_v1 = v1.Unit()
    print(unit_v1)

    zero_vector = Vector(0, 0)
    try:
        zero_vector.Unit()
    except ValueError as e:
        print(str(e))



V1 = Vector(1, 2)
result1 = V1.unit()
print("Instructor unit V1:", result1)

V1 = Vector(1, 2)
V1 = V1.unit()
print("Student unit V1:", V1)

assert str(V1) == "(0.45, 0.89)"