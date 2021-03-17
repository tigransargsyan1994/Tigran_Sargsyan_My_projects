# 1 / 2 + 3 / 4 = 5 / 4

class ratio_numbers:
    def __init__(self, t, b):
        self.top = t
        self.bottom = b

    def __mul__(self, other):
        return ratio_numbers(self.top * other.top, self.bottom * other.bottom)

    def __add__(self, other):
        new_num = ratio_numbers(0, 0)
        new_num.bottom = self.bottom * other.bottom
        new_num.top = self.bottom * self.top + self.bottom * other.top
        return new_num


x = ratio_numbers(1, 2)
y = ratio_numbers(1, 3)
sum = x + y #  x.add(y)
mul = x * y
print(sum.top, "/", sum.bottom)
print(mul.top, "/", mul.bottom)

