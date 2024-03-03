languages = ["Python", "Java", "Kotlin", "Javascript"]

print(languages)

print(languages[0])

print(languages[-2])

#Add Elements to a Python List

#1. Using append()
# The append() method adds an item at the end of the list.
# For example,
languages.append("React")

print("After append:",languages)

# 2. Using extend()
# We use the extend() method to add all items of one list to another. For example,
list2 = ["Ruby","PHP","Laravel"]
languages.extend(list2)
print("List after extend:",languages)

