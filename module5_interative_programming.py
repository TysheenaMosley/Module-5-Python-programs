# Module 5 Lab Activity - Iterative Programming
# Name: Tysheena Mosley
# Date: 02/22/2026
# This program solves 5 iterative programming problems using loops.

print("\n--- Problem 1 ---")

for i in range(100):
    print("Hello World")
print("\n--- Problem 2 ---")

numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

print("Each number:")
for num in numbers:
    print(num)

print("Each number and its square:")
for num in numbers:
    print(num, "squared is", num * num)
print("\n--- Problem 4 ---")

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("Divisible by both")
    elif i % 3 == 0:
        print("Divisible by three")
    elif i % 5 == 0:
        print("Divisible by five")
    else:
        print(i)
print("\n--- Problem 3 ---")

import turtle

# Ask user for information
sides = int(input("Enter number of sides: "))
length = int(input("Enter side length: "))
line_color = input("Enter line color: ")
fill_color = input("Enter fill color: ")

# Create turtle object
t = turtle.Turtle()

t.color(line_color)
t.fillcolor(fill_color)

# Calculate angle
angle = 360 / sides

# Draw shape
t.begin_fill()
for i in range(sides):
    t.forward(length)
    t.right(angle)
t.end_fill()

print("\n--- Problem 5 ---")



t.penup()

t.goto(0, -150)

t.pendown()



t.color("purple")



for i in range(36):

    t.forward(100)

    t.right(170)



turtle.done()

