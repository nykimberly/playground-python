#Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

#Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

"""
4
Prashant
32
Pallavi
36
Dheeraj
39
Shivam
40
"""

if __name__ == '__main__':
    grades = set()
    grades_students = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.add(score)
        grades_students[score] = grades_students.get(score, [])
        grades_students[score].append(name)
    grades = sorted(list(grades))
    runner_up_students = sorted(grades_students[grades[1]])
    for val in runner_up_students:
        print(val)
