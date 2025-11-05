# Write a python program that takes from a user 5 inputs (maths, eng, swa, sci, sos). 
# Create a function that calculates the total marks another the average marks ,
# then a functions that finds the grade according to the table below.
# Use the value from total to get the average and average to find the grade.

def user_inputs(math,eng,swa,sci,sos):
    return(math,eng,swa,sci,sos)

math = int(input("Math: "))
eng = int(input("English: "))
swa = int(input("Kiswahili: "))
sci = int(input("Science: "))
sos = int(input("Social: "))

total_marks = math + eng + swa + sci + sos
print(total_marks)

average = total_marks/5
print(average)
