class Dog:

    species = 'mammal'

    def __init__(self, n, a):

        self.name = n
        self.age = a

    def print(self):
        print(self.name, self.age)
x = Dog('Rex', 2)
y = Dog('Jack', 3)

# print(x.name, x.age)

x.print()
y.print()