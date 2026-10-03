# Muhammad Suffyan Khan
# DATA 602 - Advanced Programming Techniques
# Assignment #3
# Instructor: Nicholas Schettini


# ------------------------------------------------------------
# Q1: Meal recommendation using conditional statements
# ------------------------------------------------------------

print("Q1: Meal Recommendation")

meal = input("Enter breakfast, lunch, or dinner: ").strip().lower()

if meal == "breakfast":
    print("How about some eggs, toast, and fruit?")
elif meal == "lunch":
    print("How about a grilled chicken sandwich and a salad?")
elif meal == "dinner":
    print("How about some chicken, rice, and vegetables?")
else:
    print("I only have recommendations for breakfast, lunch, or dinner.")


# ------------------------------------------------------------
# Q2: Student employee payroll calculation
# ------------------------------------------------------------

print("\nQ2: Student Employee Payroll")

hours_worked = float(input("Enter the number of hours worked: "))
hourly_rate = float(input("Enter the hourly pay rate: $"))

if hours_worked > 20:
    regular_pay = 20 * hourly_rate
    overtime_hours = hours_worked - 20
    overtime_pay = overtime_hours * hourly_rate * 1.5
    gross_pay = regular_pay + overtime_pay
else:
    regular_pay = hours_worked * hourly_rate
    overtime_hours = 0
    overtime_pay = 0
    gross_pay = regular_pay

print(f"Regular pay: ${regular_pay:.2f}")
print(f"Overtime hours: {overtime_hours:.2f}")
print(f"Overtime pay: ${overtime_pay:.2f}")
print(f"Gross pay: ${gross_pay:.2f}")


# ------------------------------------------------------------
# Q3: Multiply a number by 10
# ------------------------------------------------------------

print("\nQ3: Times Ten Function")


def times_ten(number):
    product = number * 10
    print(f"{number} multiplied by 10 is {product}.")


number = float(input("Enter a number to multiply by 10: "))
times_ten(number)


# ------------------------------------------------------------
# Q4: Debug the calorie program
# ------------------------------------------------------------

print("\nQ4: Calorie Calculator")


def showCalories(calories1, calories2):
    total_calories = calories1 + calories2
    print(
        "The total calories you ate today:",
        format(total_calories, ".2f")
    )


def main():
    calories1 = float(
        input("How many calories are in the first food? ")
    )
    calories2 = float(
        input("How many calories are in the second food? ")
    )
    showCalories(calories1, calories2)


main()


# ------------------------------------------------------------
# Q5: Calculate the total of the number series
# ------------------------------------------------------------

print("\nQ5: Number Series")

series_total = 0

for numerator in range(1, 31):
    denominator = 31 - numerator
    series_total += numerator / denominator

print(f"The total of the series is {series_total:.6f}.")


# ------------------------------------------------------------
# Q6: Calculate the area of a triangle
# ------------------------------------------------------------

print("\nQ6: Triangle Area")


def triangle_area(base, height):
    area = 0.5 * base * height
    print(f"The area of the triangle is {area:g}.")


triangle_area(5, 4)