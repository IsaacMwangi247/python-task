# Email as input
email = input("Enter your email: ")
if email.count("@") >1:
    print("Invalid email")
elif email.count("@") == 0:
    print("Invalid email")
else:
    print(f"Your email {email} is valid")