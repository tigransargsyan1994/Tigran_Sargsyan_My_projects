
students = {}

def read_input_data():
    scores_file = open("scores.txt", "r")
    grades_file = open("grades.txt", "r")

    scores_file.readline()

    for line in scores_file:
        values = line.strip().split(",")
        if values[0] != "":
           students[values[0]] = values[1:]

    grades_file.readline()

    for line in grades_file:
       values = line.strip().split(",")
       if values[0] != "":
           students[values[0]].append(values[1:])

# a * score + b * presence + c * avg grade
def get_max_score(a, score, b, presence, c, grade):
    return a * score + b * presence + c * grade

def avg(l):
    if len(l) == 0:
        return 0
    return sum([int(x) for x in l]) / len(l)

def find_best_student():
    print(students)
    max_val = 0
    id = -1
    for key, value in students.items():
        #print(key, value)
        val = get_max_score(0.2, int(value[2]), 0.2, int(value[3]), 0.6, avg(value[4]))
        if val > max_val:
            max_val = val
            id = key

    print(id, ":", students[id][0])

# how to read from file again ?

read_input_data()
find_best_student()
