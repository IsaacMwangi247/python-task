# Write a program to reverse a string

# value = input("Enter a string: ")

# def reverse_string(s):
#     return s[::-1]

# reversed_string = reverse_string(value)
# print("Your new reversed string is", reversed_string)



# write a program to print even numbers from a list

list = [1,2,3,4,5,6,7,8]
def get_even(list):
    even_numbers = []
    for i in list:
        if i%2 == 0:
            even_numbers.append(i)
    return even_numbers
even = get_even(list)
print(even)


# getting squares

squares_list = []
for i in range(1,31):
    squares_list.append(i**2)
    return squares_list


