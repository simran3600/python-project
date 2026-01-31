# number divisible by 3 from 1 to 1000

# start counting from 1
number = 1
# Loop until 1000
while number <= 1000:
    # Check if the number is divisible by 3
    if number % 3 == 0:
        print(number)
    # Go to the next number
    number = number + 1



#convert inches to centimeters

while True:
    inches = float(input("Enter inches (negative value to stop): "))

    if inches < 0:
        print("Program ended.")
        break

    centimeters = inches * 2.54
    print(inches, "inches =", centimeters, "cm")



# find the smallest and largest number

# Initialize variables to None
smallest = None
largest = None

while True:
    n = input("Enter a number (or press Enter to quit): ")
    if n == "":
        break
    n = float(n)

    if smallest is None or n < smallest:
        smallest = n
    if largest is None or n > largest:
        largest = n

print("Smallest number:", smallest)
print("Largest number:", largest)



# random integer between 1 and 10

import random

# Computer picks a number between 1 and 10
number = random.randint(1, 10)

while True:
    guess = int(input("Guess the number (1-10): "))

    if guess == number:
        print("Correct! You guessed it.")
        break
    elif guess < number:
        print("Too low! try it again ")
    else:
        print("Too high! try it again ")



#username and password

# Correct credentials
correct_username = "python"
correct_password = "rules"

attempts = 0

while attempts < 5:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Welcome!")
        break  # if login is correct then stop the loop
    else:
        print("Incorrect username or password. Try again.")
        attempts += 1

# If user used all 5 attempts
if attempts == 5:
    print("Access denied.")



# random points to generate and calculate the value of pie

import random

# Ask the user for number of points
total_points = int(input("Enter the number of random points: "))

inside_circle = 0
count = 0

while count < total_points:
    # Generate random x and y between -1 and 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    # Check if point is inside the circle
    if x ** 2 + y ** 2 <= 1:
        inside_circle += 1

    count += 1  # Increase the counter

# Calculate approximate value of pi
pi_approx = 4 * inside_circle / total_points

print("Approximation of pi:", pi_approx)





