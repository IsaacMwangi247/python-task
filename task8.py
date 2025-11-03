# Write a program that takes as input the speed of a car
speed = float(input("Enter car speed: "))
# speed limit
limit = 70

if speed <= limit:
    print("OK")
else:
    # calculating points as the speed exceeds the limit 70
    points = (speed-limit)// 5
 
    if points <1:
        print("Your demerit point: 1")
    if points <12:
        print(f"Demerit points: {points}")
    else:
        print(f"Licence suspended after attaining {points}")
