# Write a program that takes input of someone's basic salary and benefits, 
# adds them to find the gross salary 
# then uses  the gross salary to find the NHIF rate

def salary_cal():
    basic_salary = float(input("Enter basic salary: "))
    benefits = float(input("Enter benefits: "))
    gross_salary = basic_salary + benefits
    

    # NHIF Rate
    if gross_salary <=5999:
        nhif = "150"
    elif gross_salary <=7999:
        nhif = "300"
    elif gross_salary <=11999:
        nhif = "400"
    elif gross_salary <=14999:
        nhif = "500"
    elif gross_salary <=19999:
        nhif = "600"
    elif gross_salary <=24999:
        nhif = "750"
    elif gross_salary <=29999:
        nhif = "850"
    elif gross_salary <=34999:
        nhif = "900"
    elif gross_salary <=39999:
        nhif = "950"
    elif gross_salary <=44999:
        nhif = "1000"
    elif gross_salary <=49999:
        nhif = "1100"
    elif gross_salary <=59999:
        nhif = "1200"
    elif gross_salary <=69999:
        nhif = "1300"
    elif gross_salary <=79999:
        nhif = "1400"
    elif gross_salary <=89999:
        nhif = "1500"
    elif gross_salary <=99999:
        nhif = "1600"
    elif gross_salary >=100000:
        nhif = "1700"

    print(f"Gross salary: {gross_salary}")
    print(f"NHIF Rate: {nhif}")

    # NSSF Rate calculation
    def nssf_calc():
        nssf_rate = gross_salary*6/100
        if gross_salary <18000:
            print("Not elligible for NSSF Deductions")
        else:
            print(f"Your NSSF Rate is {nssf_rate}")
    
        # NHDF calculation
        def nhdf_calc():
            NHDF = round(gross_salary *  0.015, 2)
            print(f"Your NHDF is {NHDF}")
        
            # Taxable income calculation
            # convert the nhif string to an integer
            def taxable():
                new_nhif = int(nhif)
                taxable_income = gross_salary - (nssf_rate + NHDF + new_nhif)
                print(f"Your taxable income is: {taxable_income}")

            taxable()

            # Task 19: PAYEE



        nhdf_calc()
    nssf_calc()
salary_cal()
