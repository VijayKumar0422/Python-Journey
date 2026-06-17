class Student:

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("\nStudent Details")
        print("Name :", self.name)
        print("Roll No :", self.roll_no)
        print("Marks :", self.marks)

name = input("Enter Name: ")
roll_no = input("Enter Roll Number: ")
marks = float(input("Enter Marks: "))

s1 = Student(name, roll_no, marks)

s1.display()