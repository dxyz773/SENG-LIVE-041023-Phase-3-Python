# Sequence Types
# Note: use print() to execute the examples. Comment out examples after they've been demoed.

# Creating Lists
# 1. ✅ Create a list of 10 pet names
pet_names = [
    "Rose",
    "Meow Meow Beans",
    "Mr.Legumes",
    "Luke",
    "Lea",
    "Princess Grace",
    "Spot",
    "Tom",
    "Mini",
    "Paul",
]

# Reading Information From Lists
# 2. ✅ Return the first pet name
# print(pet_names[0])

# 3. ✅ Return all pet names beginning from the 3rd index
# print(pet_names[2 : len(pet_names)]) or print(pet_names[2:])

# 4. ✅ Return all pet names before the 3rd index
# print(pet_names[0:3]) or print(pet_names[3:])

# 5. ✅  Return all pet names beginning from the 3rd index and up to the 7th
# print(pet_names[2:7])

# 6. ✅ Find the index of a given element
# print(pet_names.index("Spot"))

# 7. ✅ Reverse the original list
# pet_names.reverse()
# print(pet_names)

# 8. ✅ Return the frequency of a given element
# print(pet_names.count("Lea"))

# Updating Lists
# 9. ✅ Change the first element to all uppercase
# print(pet_names[0].upper())

# 10. ✅ Append a new name to the list
# pet_names.append("Rocky")
# print(pet_names)

# 11. ✅ Add a new name at a specific index
# pet_names.insert(2, "Spike")
# print(pet_names)

# 12. ✅ Add two lists together
# print(pet_names + ["Tori", "Rover"])

# 13. ✅ Remove the final element from the list
# pet_names.pop()
# print(pet_names)

# 14. ✅ Remove element by specific index
# del pet_names[1] or pet_names.remove(pet_names[0]) or pet_names.pop(0)
# print(pet_names)

# 15. ✅ Remove a specific element
# pet_names.remove("Spot")
# print(pet_names)

# 16. ✅ Remove all pet names from the list
# pet_names.clear()
# print(pet_names)

# Tuple
# 📚 Review With Students:
# Mutable, Immutable, Changeable, Unchangeable

# 17. ✅ Create a Tuple of pet 10 ages
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# 18. ✅ Print the first pet age
# print(my_tuple[0])

# Testing Changeability
# 19. ✅ Attempt to remove an element with ".pop" (should error)


# 20. ✅ Attempt to change the first element (should error)


# Tuple Methods
# 21. ✅ Return the frequency of a given element
# print(my_tuple.count(3))

# 22. ✅ Return the index of a given element
# print(my_tuple.index(5))

# 23. ✅ Create a Range
# Note:  Ranges are primarily used in loops
# ten = range(10)
# print(ten)

# Demo Sets (Stretch Goal)
# 24. ✅ Create a set of 3 pet foods
# pet_food = ["treats", "bone", "fruit", "fruit"]
# set_pet_food = set(pet_food)
# print(set_pet_food)

# Demo Dictionaries
# Creating
# 25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_rose = {"name": "rose", "age": 11, "breed": "domestic long "}


# 26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_spot = dict(name="Spot", age=25, breed="boxer")


# Reading
# 27. ✅ Print the pet attribute of "name" using bracket notation
# print(pet_info_rose["name"])

# 28. ✅ Print the pet attribute of "age" using ".get"
# Note: ".get" is preferred over bracket notation in most cases because it will return "None" instead of an error
# print(pet_info_rose.get("age"))

# Updating
# 29. ✅ Update the pets age to 12
# pet_info_rose["age"] = 12
# print(pet_info_rose)


# 30. ✅ Update the other pets age to 26
# pet_info_spot["age"] = 26
# print(pet_info_spot)

# Deleting
# 30. ✅ Delete a pets age using the "del" keyword
# del pet_info_spot["age"]
# print(pet_info_spot)

# 31. ✅ Delete the other pets age using ".pop"
# pet_info_rose.pop("age")
# print(pet_info_rose)

# 32. ✅ Delete the last item in the pet dictionary using "popitem()"
# pet_info_rose.popitem()
# print(pet_info_rose)

# Demo Loops
pet_info = [
    {
        "name": "rose",
        "age": 11,
        "breed": "domestic long-haired",
    },
    {
        "name": "spot",
        "age": 25,
        "breed": "boxer",
    },
    {
        "name": "Meow Meow Beans",
        "age": 2,
        "breed": "domestic long-haired",
    },
]

# 33. ✅ Loop through a range of 10 and print every number within the range

# for i in range(10):
#     print(i)


# 34. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number
# for i in range(50, 60, 2):
#     print(i)


# 35. ✅ Loop through the "pet_info" list and print every dictionary
# for i in pet_info:
#     print(i)


# 36. ✅ Create a function that takes a list as an argument
# The function should use a "for" loop to loop through the list and print every item
# Invoke the function and pass it "pet_names" as an argument
# def print_dict(list):
#     for i in list:
#         print(i)


# print_dict(pet_info)

# 37. ✅ Create a function that takes a list as an argument. (simple example)
# The function should define a counter and set it to 0
# Create a "while" loop
# The loop will continue as long as the counter is less than the length of the list
# Every loop should increase the count by 1
# Return the counter


# def count(list):
#     i = 0
#     while i < len(list) -1:
#         i += 1
#     return i


# example = count([1, 2, 3, 4, 5, 6, 7, 8])
# print(example)

# 38. ✅ Create a function that updates the age of a given pet
# The function should take a list of "dict"s, "name" and "age" as parameters
# Create am index variable and set it to 0
# Create a while loop
# The loop will continue so long as the list does not contain a name matching the "name" param and the index is less then the length of the list
# Every list will increase the index by 1
# If the dict containing a matching name is found, update the item's age with the new age
# Otherwise, return 'pet not found'


def check(dictionary, name, age):
    i = 0
    while i < len(dictionary):
        if dictionary[i]["name"] == name:
            dictionary[i]["age"] = age
        else:
            return "pet not found"
        i += 1


# check_return = check(pet_info, "bob", 100)
# print(pet_info, check_return)
# map like

# 39. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase

test = [key["name"].upper() for key in pet_info]
print(test)


# 40. ✅ Use list comprehension to find a pet named spot

test_1 = [key for key in pet_info if key["name"] == "spot"]
print(test_1)

# filter like
# 41. ✅ Use list comprehension to find all of the pets under 3 years old
test_2 = [pet["name"] for pet in pet_info if pet["age"] < 3]
print(test_2)

# 43. ✅ Create a generator expression matching the filter above. Compare and contrast the generator to the list comprehension.
test_3 = (pet["name"] for pet in pet_info if pet["age"] < 3)
for i in test_3:
    print(i)
