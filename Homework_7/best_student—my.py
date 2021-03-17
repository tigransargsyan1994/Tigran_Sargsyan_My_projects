
students = {}

def read_input_data():
    scores_file_1 = open("Anna_Ghazaryan_scores.txt", "r")
    grades_file_1 = open("Anna_Ghazaryan_grades.txt", "r")
    scores_file_2 = open("Armen_Galstyan_scores.txt", "r")
    grades_file_2 = open("Armen_Galstyan_grades.txt", "r")


    scores_file_1.readline()
    scores_file_2.readline()




    for line in scores_file_1:
        values = line.strip().split(",")
        if values[0] != "":
           students[values[0]] = values[1:]

    for line in scores_file_2:
        values = line.strip().split(",")
        if values[0] != "":
           students[values[0]] = values[1:]


    grades_file_1.readline()
    grades_file_2.readline()

    for line in grades_file_1:
       values = line.strip().split(",")
       if values[0] != "":
           students[values[0]].append(values[1:])

    for line in grades_file_2:
       values = line.strip().split(",")
       if values[0] != "":
           students[values[0]].append(values[1:])

    # for k, v in students.items():
    #     print(k, v)

# a * score + b * presence + c * avg grade
def get_max_score(a, score, b, presence, c, grade):
    return a * score + b * presence + c * grade

def avg(l):
    if len(l) == 0:
        return 0
    return sum([int(x) for x in l]) / len(l)

def find_best_student():
    # print(students)
    max_val = 0
    name = -1
    for key, value in students.items():
        #print(key, value)
        val = get_max_score(0.2, int(value[1]), 0.2, int(value[2]), 0.6, avg(value[3]))
        if val > max_val:
            max_val = val
            name = key

    print(name)

# how to read from file again ?

read_input_data()

find_best_student()
