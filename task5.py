# Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables
# x = int(input("First input: "))
# y = int(input("Second input: "))
# z = int(input("Third input: "))
# user_inputs = [x, y, z]

# largest = sorted(user_inputs)[-1]
# print(largest)


def user_inputs(x,y,z):
    return(x,y,z)[-1]

x = int(input("First input: "))
y = int(input("Second input: "))
z = int(input("Third input: "))

largest = user_inputs(x,y,z)
print(largest)
