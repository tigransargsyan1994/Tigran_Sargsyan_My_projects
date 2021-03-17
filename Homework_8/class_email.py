class student:
    def __init__(self, name, year, p, s, grades):

        self.name = name
        self.year_of_entry = year
        self.presence = p
        self.score = s
        self.grades = grades

    def grades_avg(self):
        if len(self.grades) == 0:
            return 0
        return sum([int(x) for x in self.grades]) / len(self.grades)

    def get_max_score(self, a, b, c):
        return a * self.score + b * self.presence + c * grades

    def set_grades(self, l):
        self.grades = l

students = {}


def read_input_data():
    scores_file = open("scores.txt", "r")
    grades_file = open("grades.txt", "r")

    scores_file.readline()

    for line in scores_file:
        values = line.strip().split(",")
        if values[0] != "":
            st = student(values[1], values[3], values[4])
            students[values[0]] = st

    grades_file.readline()

    for line in grades_file:
       values = line.strip().split(",")
       if values[0] != "":
           students[values[0]].set_grades(values[1:])

