numbers = {2,3,4,6,3,5,35,5,6,6,8,2,53,1}

print("Initial Set Numbers:",numbers)
# we can see there are no duplicate items in the set as a set cannot contain duplicates.

numbers.add(909)
print("Updated Set:",numbers)


# UPDATE PYTHON SET
# The update() method is used to update the set with items other collection types (lists, tuples, sets, etc).
companies = {"Nike","Bentley"}

tech_companies = {"Apple","Microsoft","Google","apple","Apple"}
companies.update(tech_companies)
print(companies)
# Here, all the unique elements of tech_companies are added to the company's set.


for company in companies:
    print(company)


# Union of Two Sets
A = {1,3,4}
B = {2,5,6}
print("Union using |:", A|B)

# Set Intersection
print("Intersection using &:",A&B)
print("Intersection using &:",A.intersection(B))