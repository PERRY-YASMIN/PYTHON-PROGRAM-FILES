print("URK24CS1044 SHAIK YASMIN")
n=int(input("Enter the number of students:"))
# List to store student details
students = [(input(f"Enter name of student {i+1}: "),
             input(f"Enter registration number of student {i+1}: "),
             float(input(f"Enter CGPA of student {i+1}: "))) for i in range(n)]

# Function to display student details
def display_students(student_list):
    for student in student_list:
        print(f"Name: {student[0]}, RegNo: {student[1]}, CGPA: {student[2]}")

# Menu-driven option
while True:
    print("\nMenu:\n1. Sort by Name\n2. Sort by RegNo\n3. Sort by CGPA\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        students.sort(key=lambda student: student[0])
        print("\nSorted by Name:")
        display_students(students)
    elif choice == '2':
        students.sort(key=lambda student: student[1])
        print("\nSorted by Registration Number:")
        display_students(students)
    elif choice == '3':
        students.sort(key=lambda student: student[2], reverse=True)
        print("\nSorted by CGPA:")
        display_students(students)
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please try again.")
