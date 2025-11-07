basic_salary = float(input("Enter basic salary: "))
benefits = float(input("Enter benefits: "))

def get_gross_salary(basic,benefits):
    return basic + benefits

def get_nhif(gross):
    if gross >= 0 and gross <= 5999:
        nhif = 150
    elif gross >= 6000 and gross <= 7999:
        nhif = 300
    elif gross >= 8000 and gross <= 11999:
        nhif = 400
    elif gross >= 12000 and gross <= 14999:
        nhif = 500
    elif gross >= 15000 and gross <= 19999:
        nhif = 600
    elif gross >= 20000 and gross <= 24999:
        nhif = 750
    elif gross >= 25000 and gross <= 29999:
        nhif = 850
    elif gross >= 30000 and gross <= 34999:
        nhif = 900
    elif gross >= 35000 and gross <= 39999:
        nhif = 950
    elif gross >= 40000 and gross <= 44999:
        nhif = 1000
    elif gross >= 45000 and gross <= 49999:
        nhif = 1100
    elif gross >= 50000 and gross <= 59999:
        nhif = 1200
    elif gross >= 60000 and gross <= 69999:
        nhif = 1300
    elif gross >= 70000 and gross <= 79999:
        nhif = 1400
    elif gross >= 80000 and gross <= 89999:
        nhif = 1500
    elif gross >= 90000 and gross <= 99999:
        nhif = 1600
    else:
        nhif = 1700
    return nhif

gross_salary = get_gross_salary(basic_salary,benefits)
nhif = get_nhif(gross_salary)


# NSSF Rate  using 6% of the Gross Salary
def get_nssf(gross):
    if gross_salary >18000:
        nssf = gross_salary*0.06
        return nssf
    else:
        return "Not elligible"
nssf = get_nssf(gross_salary)
    
# calculate an individual’s NHDF
def get_nhfd(gross):
    nhfd = gross_salary*0.015
    return nhfd
nhfd = get_nhfd(gross_salary)

# Calculate the taxable income.i.e taxable_income = gross salary - (NSSF + NHDF + NHIF) 

def get_taxable_income():
    taxable_income = gross_salary - (nssf+nhfd+nhif)
    return taxable_income
taxable_income = get_taxable_income()

# PAYE Calculation

def get_paye():
    if gross_salary < 24000:
        return "Not eligible"


print("Gross salary is Ksh. ",gross_salary)
print("NHIF is Ksh. ",nhif)
print("NSSF Rate: ", nssf)
print("NHFD is: ", nhfd)
print("Taxable income: ", taxable_income)