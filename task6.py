# Write a program that lets the user input a password. Give them only 4 attempts
# password == "admin@123"

max_attempts = 4
attempts = 0

# while loop
while attempts < max_attempts:
    password = input("Enter your password: ")
    if password == "admin@123":
        print("Access granted")
        break 
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        if remaining_attempts >0:
            print("Wrong password. Try again")
        else:
            print("Account blocked")
        
