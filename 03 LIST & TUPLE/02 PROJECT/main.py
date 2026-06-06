students = ["Rahul", "Vijay", "Priya"]

new_student = input("Enter new student name: ")
students.append(new_student)
print("student List")
for student in students:
    print(student)

print("Total Students = ", len(students))
