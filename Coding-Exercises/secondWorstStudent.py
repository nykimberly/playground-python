#Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

#Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    
    phys_grades = []
    min_grade = float("inf")
    runner_up = float("inf")
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score < min_grade:
            runner_up = min_grade
            min_grade = score
        phys_grades.append([name, score])
    
    runner_up_students = []
    for phys_grade in phys_grades:
        if phys_grade[1] == runner_up:
            runner_up_students.append(phys_grade[0])
    
    runner_up_students.sort()
    for student in runner_up_students:
        print(student)