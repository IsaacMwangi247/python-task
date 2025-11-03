# Write a program that prints the largest of 4 inputs taken as input from a user.
value_1 = input("Enter 1st value: ")
value_2 = input("Enter 2nd value: ")
value_3 = input("Enter 3rd value: ")
value_4 = input("Enter 4th value: ")
list= [value_1, value_2, value_3, value_4]

largest = sorted(list)[-1]
print(largest)