# Άσκηση 4: έρευνα άγχους μαθημάτων από το stress.txt

def find_epl_courses(courses):
    epl = []
    for course in courses:
        if course[0:3] == "EPL":
            epl.append(course)
    epl.sort()
    return epl


def find_highest_stress_course(courses, scores):
    high_score = scores[0]
    high_course = courses[0]
    for i in range(len(scores)):
        if scores[i] > high_score:
            high_score = scores[i]
            high_course = courses[i]
    print(f"Το μάθημα με τη ψηλότερη βαθμολογία άγχους είναι το {high_course} με βαθμολογία {high_score}")


def find_high_stress_courses(courses, scores, stress_grade):
    result = []
    for i in range(len(scores)):
        if scores[i] > stress_grade:
            result.append(courses[i])
    return result


def find_average_epl_stress_grade(courses, scores):
    total = 0
    count = 0
    for i in range(len(courses)):
        if courses[i][0:3] == "EPL":
            total = total + scores[i]
            count = count + 1
    return total / count


def save_to_file(scores):
    f = open("output.txt", "w")
    average = sum(scores) / len(scores)
    f.write(str(max(scores)) + " " + str(min(scores)) + " " + str(average))
    f.close()


courses = []
scores = []
f = open("stress.txt")
for line in f:
    parts = line.strip().split(",")
    courses.append(parts[0])
    scores.append(int(parts[1]))
f.close()

print(f"Στην έρευνα συμμετέχουν {len(courses)} μαθήματα")

epl = find_epl_courses(courses)
print("Μαθήματα Πληροφορικής:", end=" ")
for course in epl:
    print(course, end=" ")
print()

find_highest_stress_course(courses, scores)

stress_grade = int(input("Δώσε τη βαθμολογία άγχους (0-100): "))
high = find_high_stress_courses(courses, scores, stress_grade)
print(f"Το πλήθος των μαθημάτων με βαθμολογία άγχους > {stress_grade} είναι {len(high)} . Τα μαθήματα είναι τα {high}")

average = find_average_epl_stress_grade(courses, scores)
print(f"Ο μέσος όρος βαθμολογίας άγχους των μαθημάτων της πληροφορικής είναι {average}")

save_to_file(scores)
