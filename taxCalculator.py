basic_salary = float(input("Enter basic salary: "))
benefits = float(input("Enter benefits : "))

def get_gross(basic,benefits):
    return basic + benefits

gross_salary = get_gross(basic_salary,benefits)
print("Gross salary: ", gross_salary)

def get_nhif(gross):
    if gross > 0 and gross <= 5999:
        nhif = 150
    elif gross >= 6000 and gross <= 7999: