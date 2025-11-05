# display  either “odd” or “even” to the user
# x = int(input("Enter a number: "))

# if x %2 == 0:
#     print("Even")
#     if x %4 == 0:
#         print("Divisible by 4")
# else:
#     print("Odd")

def odd_even(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

# Input from the user
try:
    user_input = int(input("Enter a number: "))
    result = odd_even(user_input)
    print(f"The number {user_input} is {result}.")
except ValueError:
    print("Please enter a valid integer.")

