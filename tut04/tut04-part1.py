#function to add a student
def add_student(students, name, grades):
    name = name.lower()
    students[name] = grades

#function to upgrade grades for any student
def update_grades(students, name, new_grades):
    name = name.lower()
    if name in students:
        students[name] = new_grades
    else:
        print(f"Student {name} not found!")

#function to calculate average for each student
def calculate_average(grades):
    return sum(grades) / len(grades)

#function to print all student details
def print_all_students(students):
    for name, grades in students.items():
        avg_grade = calculate_average(grades)
        print(f"{name.capitalize()} - Average: {avg_grade:.2f}")

#function to sort students based on average grades
def sort_students_by_grades(students):
    sorted_students = list(students.items())
    for i in range(len(sorted_students)):
        for j in range(i + 1, len(sorted_students)):
            if calculate_average(sorted_students[i][1]) < calculate_average(sorted_students[j][1]):
                sorted_students[i], sorted_students[j] = sorted_students[j], sorted_students[i]
    return sorted_students

# Taking user input
students = {}

while True:
    action = input("Choose an action: add/update/print/sort/exit: ").lower()

    if action == 'add':
        name = input("Enter student's name: ")
        grades = list(map(int, input("Enter grades separated by space: ").split()))
        add_student(students, name, grades)

    elif action == 'update':
        name = input("Enter student's name: ")
        new_grades = list(map(int, input("Enter new grades separated by space: ").split()))
        update_grades(students, name, new_grades)

    elif action == 'print':
        print_all_students(students)

    elif action == 'sort':
        sorted_students = sort_students_by_grades(students)
        print("\nSorted Students:")
        for name, grades in sorted_students:
            print(f"{name.capitalize()} - Average: {calculate_average(grades):.2f}")

    elif action == 'exit':
        break

    else:
        print("Invalid action! Please choose again.")