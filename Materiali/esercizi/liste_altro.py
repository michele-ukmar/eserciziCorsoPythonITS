# This exercise defines a dictionary called "students" that associates student names with their grades in the form of tuples. It then creates an empty list called "a_students" that will be used to store the names of students who received an A (90 or above) average grade.
# The program iterates through the students dictionary using the items() method, which returns a list of key-value pairs in the form of tuples. For each student, the program calculates the average grade by summing the grades and dividing by the number of grades. If the average grade is 90 or above, the student's name is added to the a_students list. Finally, the program prints the list of A students.
# You can modify this exercise to include more complex operations like sorting the students by average grades, or adding more data to the dictionary such as student's address, age, and more.



# Create a dictionary of students and their grades
students = {
    "Alice": (90, 85, 80),
    "Bob": (80, 75, 70),
    "Charlie": (85, 80, 75)
}

# Create a list of students who received an A (90 or above)
a_students = []

# Iterate through the students dictionary
for name, grades in students.items():
    # Check if the student's average grade is 90 or above
    if sum(grades) / len(grades) >= 90:
        a_students.append(name)

# Print the list of A students
print(a_students)


