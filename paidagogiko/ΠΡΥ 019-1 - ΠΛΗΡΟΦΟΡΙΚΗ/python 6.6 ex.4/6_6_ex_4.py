def find_epl_courses(courses):
    result = []
    
    for course in courses:
        if course.startswith('EPL'):
            result.append(course)

    result.sort()

    return result

def find_highest_stress_course(courses, scores):
    high_score = 0
    high_course = ''
    number_of_courses = len(courses)
    
    for i, score in enumerate(scores):
        if score > high_score:
            high_score = score
            high_course = courses[i]


    print(f"Το μάθημα με τη ψηλότερη βαθμολογία άγχους είναι το {high_course} με βαθμολογία {high_score}")


def find_high_stress_courses(courses, scores, stress_grade):
    result = []

    for i, score in enumerate(scores):
        if score > stress_grade:
            result.append(courses[i])

    return result

def find_average_epl_stress_grade(courses, scores):
    epl_scores = []
    
    for i, course in enumerate(courses):
        if course.startswith('EPL'):
            epl_scores.append(scores[i])

    average = sum(epl_scores) / len(epl_scores)

    return average


def save_to_file(scores):
    maximum = max(scores)
    minimum = min(scores)
    average = sum(scores) / len(scores)

    f = open("output.txt", "w")
    f.write(str(maximum) + ' ' + str(minimum) + ' ' + str(average))

    
    

def main():
    # variables
    courses = []
    scores = []
    
    # read data from file stress.txt
    stress = open('stress.txt', 'r')
    

    for line in stress:
        lista = line.split(',')
        courses.append(lista[0])
        scores.append(int(lista[1]))
        #print(lista[0])

    print(f"Στην έρευνα συμμετέχουν {len(courses)} μαθήματα")
        
    epl_courses = find_epl_courses(courses)
    print(f"Μαθήματα Πληροφορικής: {epl_courses}")

    find_highest_stress_course(courses, scores)

    stress_grade = int(input("Δώσε τη βαθμολογία άγχους (0-100): "))

    high_stress_courses = find_high_stress_courses(
        courses, scores, stress_grade)
    print(f"Το πλήθος των μαθημάτων με βαθμολογία άγχους > {stress_grade} είναι {len(high_stress_courses)} . Τα μαθήματα είναι τα {high_stress_courses}")

    average_epl_scores = find_average_epl_stress_grade(courses, scores)
    print(f"Ο μέσος όρος βαθμολογίας άγχους των μαθημάτων της πληροφορικής είναι {average_epl_scores}")

    save_to_file(scores)
    
    


# This block runs only when the file is executed directly,
# not when it's imported as a module.
if __name__ == "__main__":
    main()
