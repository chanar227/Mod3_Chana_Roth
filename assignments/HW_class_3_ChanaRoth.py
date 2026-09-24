# MCON 141 — Homework 3
# Class 3 Concepts: if statements and Boolean logic
#
# Name: Chana Roth
# Date: 9/24/26
#
# DIRECTIONS
# 1. Open this file in Pyzo and save it with your own name in the filename.
# 2. Type your solution directly below each exercise's comment block.
# 3. For every exercise that asks for user input, place the input/conversion
#    statements in a try / except ValueError block.
# 4. Test every solution. If you do not use a function, leave comments stating
#    the additional tests you ran, because only the final run is visible.
# 5. All code must run without errors.
#
# EXTRA CREDIT (up to 2 points)
# Write your solutions inside functions where appropriate. For example:
#
# def check_weather(temperature):
#     if temperature > 80:
#         return "It is hot outside."
#     elif temperature < 60:
#         return "It is cold outside."
#     else:
#         return "The weather is mild."
#
# print(check_weather(75))  # should print: The weather is mild.
# print(check_weather(85))  # should print: It is hot outside.
# print(check_weather(50))  # should print: It is cold outside.


# ================================================================
# Exercise 1: What is x relative to y?
#
# Two variables are named x and y. Set y to 10 and x to 20.
y = 10
x = 20
# Write an if / elif / else statement that compares x and y:
# - If x is less than y, print: "x is less than y"
# - If x is equal to y, print: "x is equal to y"
# - If x is greater than y, print: "x is greater than y"
if x < y :
    print("x is less than y.")
elif x==y:
    print("x is equal to y.")
else:
    print("x is greater than y.")
# In a comment within your code, explain the result and why it occurs.
# Also test at least two other values of x and/or y, and document those tests.

#result of code will be x is greater than y becasue we set the x to = 20 and y = 10 and 20 is greater than 10.
# The other elif statemnts will be false.
#other values:
y = 20
x =10
if x < y :
    print("x is less than y.")
elif x==y:
    print("x is equal to y.")
else:
    print("x is greater than y.")
y = 15
x = 15
if x < y :
    print("x is less than y.")
elif x==y:
    print("x is equal to y.")
else:
    print("x is greater than y.")

# ================================================================
# Exercise 2: Is x odd or even?
#
# Use x = 20 (or define x again so this exercise runs independently).
x = 20
# If x is even, print: "x is even"
if x % 2 == 0:
    print("x is even")
# Otherwise, print: "x is odd"
else:
    print("x is odd")
# In a comment within your code, explain the result and why it occurs.
# Test at least one odd value as well.
#code result will show x is evenbecuase x = 20 and 20 divided by 2 leaves a remainder of 0.
x = 21
if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")

# ================================================================
# Exercise 3: Polynomials
#
# Two factors, when multiplied together, can produce a binomial.
# Given (x + a) * (x + b), where a and b are integers:
#
#      x + a
#  *   x + b
# -------------
#        xb + ab
#   x^2 + xa
# -------------
#   x^2 + (xb + xa) + ab
#
# Write a program named polynomial that asks the user for integers a and b,
# then computes and prints the expanded binomial.
#
# Example: (x + 2) * (x + 3) = x^2 + 5x + 6
#
# Remember: x^2 means "x squared."
# Use try / except ValueError for user input.
def polynomial():
    try:
        a = int(input("Enter an integer for a: "))
        b = int(input("Enter an integer for b: "))

        middle = a + b
        constant = a * b
        print(f"x^2 + {middle}x + {constant}")

    except ValueError:
        print("Error: You can only enter valid whole integers.")

polynomial()


# ================================================================
# Exercise 4: Analyze the polynomial
#
# Given integers a and b, expand (x + a)(x + b) into:
# x^2 + (xb + xa) + ab
#
# Then determine whether:
# - the middle-term coefficient (a + b) is positive, negative, or zero; and
# - the constant (a * b) is positive, negative, or zero.
#
# You may reuse your values of a and b from Exercise 3, but make this exercise
# run independently if possible. Use try / except ValueError for user input.
def analyze_polynomial():
    try:
        a = int(input("Enter an integer for a: "))
        b = int(input("Enter an integer for b: "))

        middle = a + b
        constant = a * b
        print(f"Expanded Polynomial: x^2 + {middle}x + {constant}")

        if middle > 0:
            print("The middle-term coefficient is positive.")
        elif middle < 0:
            print ("The middle-term coefficient is negative.")
        else:
            print("THe middle-term coefficient is zero. ")

        if constant > 0:
            print("The constant-term is positive.")
        elif constant < 0:
            print("The constant- term is negative.")
        else:
            print("The constant-term is zero.")

    except ValueError:
        print("Error: You can only enter valid whole integers.")

analyze_polynomial()


# ================================================================
# Exercise 5: Explore the and statement
#
# Ask the user to enter integers val1 and val2.
#
# - If both values are positive, print: "val1 and val2 are positive"
#   and print the values.
# - If both values are negative, print: "val1 and val2 are negative"
#   and print the values.
# - Otherwise, print: "The values are not both positive or both negative"
#   and print the values.
#
# Use try / except ValueError for user input.
try:
    val1 = int(input("Enter an integer for value 1: "))
    val2 = int(input("Enter an integer for value 2: "))

    if val1 > 0 and val2 > 0:
        print("Value 1 and Value 2 are positive")
        print(f"Value 1 = {val1} and Value 2 = {val2}")

    elif val1 < 0 and val2 < 0:
        print("Value 1 and Value 2 are negative")
        print(f"Value 1 = {val1} and Value 2 = {val2}")
    else:
        print("The values are both not positive or negative")
        print(f"Value 1 = {val1} and Value 2 = {val2}")

except ValueError:
    print("Error:You can only enter valid whole integers")


# ================================================================
# Exercise 6: Explore the or statement
#
# Ask the user to enter integers val1 and val2.
#
# - If val1 or val2 is positive, print: "At least one value is positive"
#   and print the values.
# - If val1 or val2 is equal to zero, print: "At least one value is zero"
#   and print the values.
# - Otherwise, print: "At least one value is negative"
#
# Use try / except ValueError for user input.

try:
    val1 = int(input("Enter an integer for value 1: "))
    val2 = int(input("Enter an integer for value 2: "))

    if val1 > 0 or val2 > 0:
        print("At least one value is positive.")
        print(f"Value 1 = {val1} and value 2 = {val2}.")
    elif val1 == 0 or val2 == 0:
        print("At least one value is zero.")
        print(f"Value 1 = {val1} and Value 2 = {val2}.")
    else:
        print("At least one value is negative.")

except ValueError:
    print("Error: You can only enter valid whole integers.")

# ================================================================
# Exercise 7: Explore not
#
# Set the following variables:
# a = True
# b = True
# c = False
#
# Evaluate and print the results of these expressions:
# 1. not (a and b)
# 2. not a or not c
# 3. not ((a and c) and b)
#
# Include a comment explaining each result.
a = True
b = True
c = False

expr1 = not (a and b)
print(f"Result for not (a and b): {expr1}")
# a and b are both true but hwne we write not it becomes false, the not changes it form true ot false

expr2 = not a or not c
print(f"The result of not a or not c is: {expr2}")
# not a becomes false and not c becomes true. since we have an or operater (only one side needs to be true) result in the end is true.

expr3 = not((a and c)and b)
print(f"The result of not ((a and c) and b) is : {expr3}")
# ( a and c ) is flase because of c. so then we have false and b, keeping it false. The not in the begining changes this to true.


# ================================================================
# Exercise 8: Voting Age and Citizenship
#
# Ask the user for their age and whether they are a citizen (yes or no).
#
# - If they are 18 or older AND a citizen, print:
#   "You are eligible to vote."
# - If they are under 18 OR not a citizen, print:
#   "You are not eligible to vote."
#
# Hint: use and for the eligibility requirements. Use try / except ValueError
# for the age input.
def voting_age_citizenship():
    try:
        age = int(input("How old are you? "))
        citizen = input("Are you a citizen? (yes/no): ").strip().lower()

        if age >= 18 and citizen == "yes":
            print("You are eligible to vote.")
        elif age < 18 or citizen == "no":
            print("You are not eligible to vote.")
            #or can do just an else: here
    except ValueError:
        print("Error: You did not enter a valid whole number by age.")

voting_age_citizenship()


# ================================================================
# Exercise 9: Number Classification
#
# Ask the user for an integer.
#
# - If it is positive and even, print: "Positive even number."
# - If it is positive and odd, print: "Positive odd number."
# - If it is negative or zero, print: "Not a positive number."
#
# Hint: combine and and or. Use try / except ValueError for user input.

def number_class():
    try:
        number = int(input("Enter your integer:"))

        if number > 0 and number % 2 == 0:
            print("Positive even number")
        elif number > 0 and number % 2 != 0:
            print("Positive odd number")
        elif number < 0 or number == 0:
            print("Not a positive number")
    except ValueError:
        print("Error: You can only enter a valid whole integer.")
number_class()

# ================================================================
# Exercise 10: Triangle Check
#
# Ask the user for three side lengths: a, b, and c.
#
# Print "Valid triangle." only if all sides are greater than 0 AND:
# - a + b > c
# - a + c > b
# - b + c > a
#
# Otherwise, print "Not a valid triangle."
#
# Hint: chain multiple and conditions. Use try / except ValueError for input.

def triangle_check():
    try:
        a = float(input("Enter a length for side a: "))
        b = float(input("Enter a length for side b: "))
        c = float(input("Enter a length for side c: "))
        if (a > 0 and b > 0 and c > 0 ) and ((a + b)>c) and ((a + c)>b) and ((b + c)>a):
            print("Valid triangle")
        else:
            print("Not a valid triangle")

    except ValueError:
        print("Error: You can only enter valid numbers.")

triangle_check()

# ================================================================
# Exercise 11: Weekend Plan Decision Tree
#
# Ask the user two questions:
# - Is it the weekend? (yes or no)
# - Do you have homework? (yes or no)
#
# Build a decision tree that prints:
# - Weekend and no homework: "Go have fun!"
# - Weekend and homework: "Do your homework first, then relax."
# - Not weekend and homework: "Focus on schoolwork."
# - Not weekend and no homework: "It's a regular day, keep learning!"
#
# Consider converting responses to lowercase so Yes, YES, and yes all work.

def weekend_tree():
    weekend = input("Is it the weekend? (yes/no): ").strip().lower()
    hw = input("Do you have homework? (yes/no): ").strip().lower()

    if weekend == "yes" and hw == "no":
        print("Go have fun!")
    elif weekend == "yes" and hw == "yes":
        print("Do your homework first, then relax.")
    elif weekend == "no" and hw == "yes":
        print("Focus on schoolwork.")
    elif weekend == "no" and hw == "no":
        print("It's a regular day, keep learning.")
    else:
        print("Error: please enter either yes or no.")

weekend_tree()







