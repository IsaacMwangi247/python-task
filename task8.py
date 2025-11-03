# Write a program that takes as input the speed of a car
speed = int(input("Enter car speed: "))
# speed limit
limit = 70

if speed <= limit:
    print("OK")
else:
    # calculating points as the speed exceeds the limit 70
    points = (speed-limit)// 5
    print(f"Your demerit points: {points}")
    # licence suspension once the demerit points reach 12
    if points >=12:
        print("Licence suspended")
