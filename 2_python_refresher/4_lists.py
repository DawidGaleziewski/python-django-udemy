# lists are arrays like datastructure in python. It is ordered set of values
dognames = ['Fido', 'Sean', "Sally", 'Mark']
print(dognames)

# Adding to array
# we add by using insert method on array. Insert accepts two params, first is the array index after which we will insert item and the second is the value itself
dognames.insert(1, 'Fafik')

print(dognames)

# We can access the item in array same as in js
print(dognames[3])

# Removing items from array
# Use del method and return the item from the array that we want to delete
del(dognames[2])
print(dognames)

# Get the length of the array
print(len(dognames))

# Hange the item in array
dognames[0] = "Fafik reborn"
print(dognames)

# Same as js lists in python can hold any datatype
testList = [False, 'test', [1,2,3], 100]