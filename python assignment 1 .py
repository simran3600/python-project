# 1.Greeting program

name = input("Enter your name: ")
print("Hello", name)

# 2. Area of a circle

radius = float(input("Enter the radius of the circle: "))
area = 3.14 * radius * radius
print("The area of the circle is:" + str(area))

#3. length, width ,perimeter and area of a rectangle

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
perimeter = 2 * (length + width)
area =  length * width
print("The perimeter of the rectangle is:" + str(perimeter))
print("The area of the rectangle is:" + str(area))

# 4. three integer numbers

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
sum_numbers = number1 + number2 + number3
product = number1 * number2 * number3
average = sum_numbers / 3
print("sum", sum_numbers)
print("product", product)
print("average", average)

#5. medieval unit mass

# Get input from user
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))
# Convert to grams
grams = (talents * 20 * 32 + pounds * 32 + lots) * 13.3

# Convert grams to kilograms and remaining grams
kilograms = int(grams // 1000)
grams = grams % 1000
# Show result
print(f"\nThe weight in modern units:\n{kilograms} kilograms and {grams} grams.")

#6. combination lock

import random

# 3-digit code (0 to 9)
code1 = ""
for i in  range(3):
    code1 += str(random.randint(0, 9))

# 4-digit code (1 to 6)
code2 = ""
for i in range(4):
    code2 += str(random.randint(1, 6))

print("3-digit code:", code1)
print("4-digit code:", code2)




