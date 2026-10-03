# Muhammad Suffyan Khan
# DATA 602 - Advanced Programming Techniques
# Assignment #1
# Instructor: Nicholas Schettini


# ------------------------------------------------------------
# Q1: Correct the syntax and logical errors
# ------------------------------------------------------------

# This program gets three test scores, calculates their average,
# and congratulates the user if the average is a high score.

HIGH_SCORE = 95

# Convert each input to a float because input() normally returns
# a string, and numerical values are required for the calculation.
test1 = float(input("Enter the score for test 1: "))
test2 = float(input("Enter the score for test 2: "))

# The original program used test3 without first defining it,
# so a third input statement is required.
test3 = float(input("Enter the score for test 3: "))

# Parentheses ensure that all three scores are added before
# dividing the total by 3.
average = (test1 + test2 + test3) / 3

print(f"The average score is {average:.2f}")

# Use HIGH_SCORE with the same capitalization as the constant
# defined at the beginning of the program.
if average >= HIGH_SCORE:
    # Both messages are indented so they appear only when
    # the average is at least 95.
    print("Congratulations!")
    print("That is a great average!")


# ------------------------------------------------------------
# Q2: Calculate the areas of two rectangles
# ------------------------------------------------------------

print("\nRectangle Area Calculator")

# Rectangle 1
length1 = float(input("Enter the length of rectangle 1: "))
width1 = float(input("Enter the width of rectangle 1: "))
area1 = length1 * width1

# Rectangle 2
length2 = float(input("Enter the length of rectangle 2: "))
width2 = float(input("Enter the width of rectangle 2: "))
area2 = length2 * width2

print(f"The area of rectangle 1 is {area1:.2f}")
print(f"The area of rectangle 2 is {area2:.2f}")


# ------------------------------------------------------------
# Q3: Display a birthday message
# ------------------------------------------------------------

# input() returns the name as a string.
name = input("\nEnter your first name: ")

# Convert the age to an integer as required.
age = int(input("Enter your age: "))

print(f"Happy birthday, {name}! You are {age} years old today!")