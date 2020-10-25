
# Dictionary is like a boject in js
dogs = {
    "Fido":8,
    "Sally": 17,
    "Sean": 2
}

print(dogs)
print(dogs["Sally"])

# deleting value from dictionary
del(dogs["Sean"])
print(dogs)

# add value
dogs["Buddy"] = 10
print(dogs)

# update value
dogs["Buddy"] = 200
print(dogs)