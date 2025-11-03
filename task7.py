# Write that prompts the user to input student marks. The input should be between 0 and 100.
student_marks = int(input("Enter student marks: "))
if student_marks <0 or student_marks>100:
    print("Invalid marks")
else:
    if student_marks > 79:
        print("Grade A")
    elif student_marks >=60:
        print("Grade B")
    elif student_marks > 49:
        print("Grade C")
    elif student_marks >= 40:
        print("Grade D")
    else:
        print("Grade E")
