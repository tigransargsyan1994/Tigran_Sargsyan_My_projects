class ratio_numbers:

    def __init__(self, t, b):
        self.top = t
        self.bottom = b

    def __mul__(self, other):
        return ratio_numbers(self.top * other.top, self.bottom * other.bottom)

    def __truediv__(self, other):
        return ratio_numbers(self.top * other.bottom, self.bottom * other.top)

    def __sub__(self, other):
        return ratio_numbers(self.top * other.bottom - other.top * self.bottom, self.bottom * other.bottom)

    def __add__(self, other):
        return ratio_numbers(self.top * other.bottom + other.top * self.bottom, self.bottom * other.bottom)

    def __gt__(self, other):
        if (self.top / self.bottom > other.top / other.bottom):
            return True
        else:
            return False

    def __str__(self):
        return self.top, self.bottom


x = ratio_numbers(1,2)
y = ratio_numbers(1,3)
summa = x + y
print(f'Sum is {summa.top} / {summa.bottom}')

mull = x * y
print(f'Product is {mull.top} / {mull.bottom}')

div = y / x
print(f'Quotient is {div.top} / {div.bottom}')

sub = x - y
print(f'Difference is {sub.top} / {sub.bottom}')


z = x + y
print(f'Z = {z.top} / {z.bottom}')   # __str__


if (x > y):
    print("x is greater than y")
elif (y > x):
    print("y is greater than x")
else:
    print('Objects are equal')
