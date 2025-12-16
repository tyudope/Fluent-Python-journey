class Apple:

    def __init__(self, count):
        self.count = count


    def __add__(self, other):
        return Apple(self.count + other.count)


    def __mul__(self, other):
        return Apple(self.count * other.count)

    def __repr__(self):
        return f"Apple {self.count}"



a = Apple(6)
b = Apple(7)

c = a + b
print(c)

d = c * b # 13 * 7 = 91
print(d)