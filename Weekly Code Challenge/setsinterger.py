# Accept user input to create two sets of integers
set1_input = input("Enter integers for set 1 separated by spaces: ")
set2_input = input("Enter integers for set 2 separated by spaces: ")

set1 = set(map(int, set1_input.split()))
set2 = set(map(int, set2_input.split()))

# Create a new set containing only the elements that are common to both sets
common_elements = set1.intersection(set2)
print("Common elements:", common_elements)
