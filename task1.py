# A = 1/2 * b * h
# b = input("Enter base: ")
# h = input("Enter height: ")
# A = 1/2 * int(b) * int(h)
# print(A)

# handle using functions
def triangle_area(b,h):
    return(0.5 * b * h)

b = float(input("Enter base: "))
h = float(input("Enter height: "))

area = triangle_area(b,h)
print(area)
triangle_area(b,h)

