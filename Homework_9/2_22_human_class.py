class Human:
    def __init__(self, gender, age, nationality, height):
        self.gender = gender
        self.age = age
        self.nationality = nationality
        self.height = height

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    def get_nationality(self):
        return self.nationality

    def get_height(self):
        return self.height

Hakob = Human('male', 19, 'Armenian', 174)

Jessica = Human('female', 24, 'American', 155)

Gerhard = Human('male', 35, 'German', 189)

print(Gerhard.get_gender())
print(Gerhard.get_age())
print(Gerhard.get_nationality())
print(Gerhard.get_height())