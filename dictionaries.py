cars = {"Mercedes":"C63 AMG",
        "VolksWagen":"GTI",
        "Range Rover":"SV200 Sport"}

print(cars)

cars["Lexus"]="LX 600"
# added a new element to cars
print("Available in the garage",cars)

del cars["Range Rover"]
print("Available in the garage",cars)

# DICTIONARY MEMBERSHIP TEST
# We can test if a key is in a dictionary or not using the keyword in. Notice that the membership test is only for the keys and not for the values.
print("Mazda" in cars)

#Iterating Through a Dictionary
# We can iterate through each key in a dictionary using a loop.
for i in cars:
    print(cars[i])