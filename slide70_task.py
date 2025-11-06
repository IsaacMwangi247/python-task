# Write a python program that takes from a user 5 inputs (maths, eng, swa, sci, sos). 
# Create a function that calculates the total marks another the average marks ,
# then a function that finds the grade according to the table below. 
# Use the value from total to get the average and average to find the grade.
# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40


maths = float(input("Enter Math score: "))
eng = float(input("Enter English score: "))
swa = float(input("Enter Kiswahili score: "))
sci = float(input("Enter Science score: "))
sos = float(input("Enter SOS score: "))

def get_total(a,b,c,d,e): 
    return a + b + c + d + e

def get_average(value):
    return value / 5

def get_grade(avg):
    if avg > 79 and avg < 100:
        return "A"
    elif avg >= 60 and avg <= 79:
        return "B"
    elif avg >= 50 and avg <= 59:
        return "C"
    elif avg >= 40 and avg <= 49:
        return "D"
    elif avg < 40:
        return "E"
    else:
        return "Invalid Mark"

total_mark = get_total(maths,eng,swa,sci,sos)
average = get_average(total_mark)
grade = get_grade(average)

print("Total mark is: ",total_mark)
print("Average mark is: ",average)
print("Final grade is: ",grade)
