# Write a program that takes input of 2 values and adds them
# valid_number = int or float

while True:
    try:
        value_1 = float(input("Enter first number: "))
        value_2 = float(input("Enter second number: "))
        print(f"The sum is equal to {value_1 + value_2}")
        break
    except ValueError:
        print("Invalid character")



