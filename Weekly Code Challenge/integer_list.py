# Accept user input to create a list of integers
user_input = input("Enter a list of integers separated by spaces: ")
integer_list = [int(x) for x in user_input.split()]

# Compute the sum of all the integers in the list
sum_of_integers = sum(integer_list)
print("Sum of the integers:", sum_of_integers)