# Day 14 --> if....else

# --> To perform any task when certain
# condition get satisfied

# 1. if....else
# 2. if else ladder
#-----> if....elif....elif......else
# 3. nested if else--> if else inside if else

# 1. if ....else

num = 2
if num % 2 == 0:
    print(num, "is even num")
else:
    print(num, "is odd num")

if "s" == "s":
    print("equal")

# 2. if else ladder

color = "Yellow"

if color == "Yellow":
    print("Entered color is ", color)
elif color == "Orange":
    print("Entered color is: ", color)
elif color == "Blue":
    print("Entered color is: ", color)
else:
    print("Entered color not exist in system!!")

# 3. Nested if else

num1 = 5
num2 = 2
num3 = 7

if num1 > num2:
    if num1 > num3:
        print(num1, "Is greatest")
    else:
        print(num3, "is greatest")
elif num2 > num1:
    if num2 > num3:
         print(num2, "Is greatest")
    else:
        print(num3, "is greatest")
else:
    print(num3, "is greatest")
    
if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)

    
