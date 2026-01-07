import random

def challenging_exercise():
    exercises = {
        "cardio": ["running", "jumping jacks", "jump rope"],
        "strength": ["push-ups", "pull-ups", "dips"],
        "flexibility": ["yoga", "pilates", "stretching"]
    }
    exercise_types = list(exercises.keys())
    chosen_type = random.choice(exercise_types)
    chosen_exercise = random.choice(exercises[chosen_type])
    reps = random.randint(10, 20)
    sets = random.randint(3, 5)
    print(f"Today's exercise: {chosen_exercise} {reps} reps, {sets} sets, {chosen_type} type")

challenging_exercise()


# This will create a function that randomly chooses an exercise from a 
# list of exercises that are grouped by type (cardio, strength, flexibility) 
# and then it will choose a random number of reps and sets. 
# Finally it will print the exercise with the reps, sets and type.
# Feel free to modify the exercise lists, sets and reps range 
# according to your preferences.


# This will choose a random exercise from a list and print it out as 
# "Today's exercise: [chosen exercise]" Each time you run the function, 
# it will give you a different exercise. Feel free to add or remove any 
# exercises from the list to suit your needs.

import random

def funny_exercise():
    exercise_list = ["Doing the Chicken Dance", "Jumping like a Kangaroo", "Wiggling like a worm", "Imitating a Monkey", "Acting like a Gorilla"]
    print("Today's exercise: " + random.choice(exercise_list))

funny_exercise()
