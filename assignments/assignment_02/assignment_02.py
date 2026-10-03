# Muhammad Suffyan Khan
# DATA 602 - Advanced Programming Techniques
# Assignment #2
# Instructor: Nicholas Schettini


# ------------------------------------------------------------
# Q1: Debug the list slice
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5]

print("Q1: List Slicing")

# numbers[1:-5] displays an empty list because the ending
# position occurs before the starting position.
print("Original output:", numbers[1:-5])

# Leaving both slice positions empty returns the entire list.
print("Corrected output:", numbers[:])


# ------------------------------------------------------------
# Q2: Calculate total weekly sales
# ------------------------------------------------------------

print("\nQ2: Weekly Sales")

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

daily_sales = []

# Ask the user to enter the sales for each day.
for day in days:
    sale = float(input(f"Enter sales for {day}: $"))
    daily_sales.append(sale)

# Calculate the total using a loop.
total_sales = 0

for sale in daily_sales:
    total_sales += sale

print(f"Total sales for the week: ${total_sales:,.2f}")


# ------------------------------------------------------------
# Q3: Sort a list of travel destinations
# ------------------------------------------------------------

print("\nQ3: Travel Destinations")

places = ["Tokyo", "Istanbul", "Dubai", "London", "Paris"]

print("Original order:", places)

places.sort()
print("Alphabetical order:", places)

places.sort(reverse=True)
print("Reverse alphabetical order:", places)


# ------------------------------------------------------------
# Q4: Course information dictionaries
# ------------------------------------------------------------

print("\nQ4: Course Information")

course_rooms = {
    "CS101": "3004",
    "CS102": "4501",
    "CS103": "6755",
    "NT110": "1244",
    "CM241": "1411"
}

course_instructors = {
    "CS101": "Haynes",
    "CS102": "Alvarado",
    "CS103": "Rich",
    "NT110": "Burke",
    "CM241": "Lee"
}

course_times = {
    "CS101": "8:00 AM",
    "CS102": "9:00 AM",
    "CS103": "10:00 AM",
    "NT110": "11:00 AM",
    "CM241": "1:00 PM"
}

course_number = input(
    "Enter a course number (CS101, CS102, CS103, NT110, or CM241): "
).strip().upper()

if course_number in course_rooms:
    print("Room number:", course_rooms[course_number])
    print("Instructor:", course_instructors[course_number])
    print("Meeting time:", course_times[course_number])
else:
    print("Course number not found.")


# ------------------------------------------------------------
# Q5: Name and email address dictionary
# ------------------------------------------------------------

print("\nQ5: Email Address Directory")

email_directory = {
    "Muhammad": "muhammad@example.com",
    "Aisha": "aisha@example.com",
    "Daniel": "daniel@example.com"
}

while True:
    print("\n1. Look up an email address")
    print("2. Add a new name and email address")
    print("3. Change an existing email address")
    print("4. Delete a name and email address")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        name = input("Enter the name to look up: ").strip().title()

        if name in email_directory:
            print(f"{name}'s email address is {email_directory[name]}.")
        else:
            print("Name not found.")

    elif choice == "2":
        name = input("Enter the new name: ").strip().title()
        email = input("Enter the email address: ").strip()

        email_directory[name] = email
        print(f"{name} was added.")

    elif choice == "3":
        name = input("Enter the name to change: ").strip().title()

        if name in email_directory:
            new_email = input("Enter the new email address: ").strip()
            email_directory[name] = new_email
            print(f"{name}'s email address was updated.")
        else:
            print("Name not found.")

    elif choice == "4":
        name = input("Enter the name to delete: ").strip().title()

        if name in email_directory:
            del email_directory[name]
            print(f"{name} was deleted.")
        else:
            print("Name not found.")

    elif choice == "5":
        print("Email directory program ended.")
        break

    else:
        print("Invalid option. Please choose a number from 1 to 5.")