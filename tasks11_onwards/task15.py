# Write a program that takes input of someone's basic salary and benefits, 
# adds them to find the gross salary 
# then uses  the gross salary to find the NHIF rate
basic_salary = float(input("Enter basic salary: "))
benefits = float(input("Enter benefits: "))
gross_salary = basic_salary + benefits
print(f"Your gross salary is {gross_salary}")
if gross_salary <=5999:
    print("NHIF RATE is 150")
elif gross_salary <=7999:
    print("NHIF RATE is 300")
elif gross_salary <=11999:
    print("NHIF RATE is 400")
elif gross_salary <=14999:
    print("NHIF RATE is 500")
elif gross_salary <=19999:
    print("NHIF RATE is 600")
elif gross_salary <=24999:
    print("NHIF RATE is 750")
elif gross_salary <=29999:
    print("NHIF RATE is 850")
elif gross_salary <=34999:
    print("NHIF RATE is 900")
elif gross_salary <=39999:
    print("NHIF RATE is 950")
elif gross_salary <=44999:
    print("NHIF RATE is 1000")
elif gross_salary <=49999:
    print("NHIF RATE is 1100")
elif gross_salary <=59999:
    print("NHIF RATE is 1200")
elif gross_salary <=69999:
    print("NHIF RATE is 1300")
elif gross_salary <=79999:
    print("NHIF RATE is 1400")
elif gross_salary <=89999:
    print("NHIF RATE is 1500")
elif gross_salary <=99999:
    print("NHIF RATE is 1600")
elif gross_salary >=100000:
    print("NHIF RATE is 1700")

