# Phone number validation

phone_number = input("Enter phone number: ")

# min_len = 8
# max_len = 13

if len(phone_number) <= 8:
    print("Invalid number. Please enter eg. 0710123456 or +254710123456")
elif len(phone_number) == 11:
    print("Invalid number. Please enter eg. 0710123456 or +254710123456")
elif len(phone_number) == 12:
    print("Invalid number. Please enter eg. 0710123456 or +254710123456")
elif len(phone_number) >13:
    print("Invalid number. Please enter eg. 0710123456 or +254710123456")
else:
    new_number = phone_number[-9:]
    combined = "+254" + new_number
    print(combined)
   
