# Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables
x = input("First input: ")
y = input("Second input: ")
z = input("Third input: ")
user_inputs = [x, y, z]

largest = sorted(user_inputs)[-1]
print(largest)




