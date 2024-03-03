letters = ("p","t","e","f","a","b")

print(letters)
# Indexing
# We can use the index operator [] to access an item in a tuple, where the index starts from 0.
print(letters[3])
#Negative Indexing
print(letters[-3])

# methods that add items or remove items are not available with tuples
print(letters.count("p"))
print(letters.index("f"))