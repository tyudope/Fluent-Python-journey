class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


    def __bool__(self):
        return bool(abs(self))


# Try

v = Vector(2,3)

print(v)
print(abs(v))
print(bool(v))

## Key insight: Python asks the object how it want to behave.




