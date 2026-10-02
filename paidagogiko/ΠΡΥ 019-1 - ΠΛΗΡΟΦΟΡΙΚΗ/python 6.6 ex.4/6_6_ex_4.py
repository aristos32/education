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
    
    for score in scores:
        score = int(score)
        if score > high_score:
            high_score = score


    print(f"Το μάθημα με τη ψηλότερη βαθμολογία άγχους είναι το {high_course} με βαθμολογία {high_score}")

def main():
    # variables
    courses = []
    scores = []
    
    # read data from file stress.txt
    stress = open('stress.txt', 'r')
    

    for line in stress:
        lista = line.split(',')
        courses.append(lista[0])
        scores.append(lista[1])
        #print(lista[0])

    print(f"Στην έρευνα συμμετέχουν {len(courses)} μαθήματα")
        
    epl_courses = find_epl_courses(courses)
    print(f"Μαθήματα Πληροφορικής: {epl_courses}")

    find_highest_stress_course(courses, scores)


# This block runs only when the file is executed directly,
# not when it's imported as a module.
if __name__ == "__main__":
    main()
