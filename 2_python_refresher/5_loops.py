dognames = ['Fido', 'Sean', 'Sally', "Mark", "Nicky", 'Saba']

# looping thru all items in a array
for dog in dognames:
    print(dog)

print("###########")

# Looping specified number of times
for index in range(2,4):
    print(dognames[index])

# While loops
age = 0
while age <= 18:
    print('age is:', age)
    age += 1