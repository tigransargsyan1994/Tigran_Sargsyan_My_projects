class ratio_numbers:

    def __init__(self, t, b):
        self.top= t
        self.bottom = b

    def __mul__(self, other):
        return ratio_numbers(self.top * other.top, self.bottom * other.bottom)

    def add(self, other):
        new_num = ratio_numbers(0,0)
        new_num.bottom = self.bottom * other.bottom
        new_num.top = self.bottom * self.top + self.bottom * other.top

        return new_num

x = ratio_numbers(1,2)
y = ratio_numbers(1,3)
sum = x.add(y)
print(sum.top, sum.bottom)

mul = x * y
print(mul.top, mul.bottom)

