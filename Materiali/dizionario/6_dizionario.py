# Step 1: Get input from the user
people = []
user_input = " "
while user_input != "":
    user_input = input("Input a tuple name and age (name, age), \
     double enter to finish: ")
    if user_input != "":
        name, age = user_input.split(",")
        people.append((name, int(age)))

# Input example: [('John', 20), ('Jane', 21), ('Jack', 20)]

# Step 2: Create a dictionary to store the age groups
age_groups = {}
for person in people:
    name, age = person
    if age not in age_groups:
        age_groups[age] = []
    age_groups[age].append(name)

# Step 3: Print the age groups
for age, names in age_groups.items():
    print("Age", age)
    for name in names:
        print("-", name)
