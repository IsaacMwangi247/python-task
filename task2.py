# display  either “odd” or “even” to the user
x = int(input("Enter a number: "))

if x %2 == 0:
    print("Even")
    if x %4 == 0:
        print("Divisible by 4")
else:
    print("Odd")
