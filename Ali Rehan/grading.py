marks = int(input("Enter your marks (0-100): "))
grade="H"

if marks >= 90 and marks <= 100 :
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
elif marks < 50 and marks >= 0:
    grade = "F"
else:
    print("Invalid marks entered.")

print("Your grade is: ", grade)