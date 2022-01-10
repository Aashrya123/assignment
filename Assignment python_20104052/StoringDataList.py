#Storing details of students in a list-
SID = int(input("Enter your SID: "))
Name = str(input("Enter your name: "))
Gender = str(input("Enter your gender(F-female, M-male, U-unknown): ")) 
Course_Name = str(input("Enter your course name: "))
CGPA = float(input("Enter your CGPA: "))

List = [SID, Name, Gender, Course_Name, CGPA]

print("Student Info", List)

