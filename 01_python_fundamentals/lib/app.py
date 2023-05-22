#!/usr/bin/env python3

# 📚 Review With Students:
# Python environment set up
# Python debugging tools
# Python datatypes

# 🚨 To enable ipdb debugging, first import "ipdb"
# import ipdb

# 1. ✅ Create a condition to check a pet's mood
# If "pet_mood" is "Hungry!", "Rose needs to be fed."
# If "pet_mood" is "Rowdy!", "Rose needs a walk."
# In all other cases, "Rose is all good."

# Note => Feel free to set your own values for "pet_mood" to view various outputs.


# def hello_world():
#     sleepy = "bear"
#     print(sleepy)
#     ipdb.set_trace()


# hello_world()


# not_interpreted_yet = "coffee"
# print(not_interpreted_yet)

pet_mood = "Tired!"
pet_name = "Rose"

# IF/ELSE STATEMENT
# if pet_mood == "Hungry!":
#     print("Rose needs to be fed")
# elif pet_mood == "Rowdy":
#     print("Rose needs a walk")
# else:
#     print("Rose is all good")

# TERNARY:
# true, if conditon else default value
# print("Rose needs to be fed") if pet_mood == "Hungry!" else print("Rose is all good")


# print("Hello world!", end=" ")
# print("Hello sun!", end="!! ")
# print("Hello sky!", end="!!!\n")

# 2. ✅ Create a ternary operator using "pet_mood" as a condition:
# If pet_food is "Hungry!" => "Rose needs to be fed."
# In all other cases => "Rose is all good."

# 3. ✅ Create a function (say_hello) that returns the string "Hello, world!"


# def say_hello(param="Hello"):
#     print(f"{param}, World!!")
#     return "Hello World!!!!"


# say_hello()

# Test invocation of "say_hello" in ipdb using "say_hello()"
# say_hello() => "Hello, world!"

# 4. ✅ Create a function (pet_greeting) that will return a string with interpolated pet's name
# Test invocation of "pet_greeting" in ipdb using "pet_greeting()"
# pet_greeting("Rose") => "Rose says hello!"
# pet_greeting("Spot") => "Spot says hello!"

# 5. ✅ Move conditional logic from Deliverable 1 into a function (pet_status) so that we may use it with different pets / moods


# def pet_status(name, mood):
#     if mood == "Hungry":
#         ipdb.set_trace()
#         return f"{name} needs to be fed"
#     elif mood == "Rowdy":
#         return f"{name} needs a walk"
#     else:
#         return f"{name} needs is all good"


# rose = pet_status("Rose", "Hungry")
# spot = pet_status("Spot", "Rowdy")
# print(rose)
# print(spot)

# Test invocation of "pet_status" in ipdb using "pet_status(pet_name, pet_mood)"
# pet_status("Rose", "Hungry!") => "Rose needs to be fed."
# pet_greeting("Spot", "Rowdy!") => "Spot needs a walk."
# pet_greeting("Bud", "Relaxed") => "Bud is all good."

# Take a moment to note that "pet_name" and "pet_mood" parameters are within Local Scope and take priority over "pet_name" and "pet_mood"
# in Global Scope.

# 6. ✅ Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors.
# If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user


# def pet_birthday(age):
#     try f"Happy Birthday! Your pet is {age+1} years old!":
#         return f"Happy Birthday! Your pet is {age+1} years old!"
#     except TypeError:
#         return "Type Error Occured"
#     finally:
#         return "It's all good!"


# pet_birthday(5)
# pet_birthday(10) => "Happy Birthday! Your pet is now 11."
# pet_birthday("oops") => "Type Error Occurred"

# Note => To view more common Python exceptions, visit https://docs.python.org/3/library/exceptions.html

# 🚨 To create an ipdb breakpoint, comment / uncomment line below:
# ipdb.set_trace()
