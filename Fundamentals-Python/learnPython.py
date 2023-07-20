# Dictionaries
dog = {"name": "Roger", "age": 8, "color": "black"}

dog['name'] = "Syd"

print(dog)
print(dog.get('color', "green"))

# Remove Item With key
# dog.pop("age")
# Remove last Item
# dog.popitem()

# Check Is Item In Dictionary
print("color" in dog)

# Keys of Dictionary
print(dog.keys())
print(list(dog.keys()))

# Values of Dictionary
print(dog.values())
print(list(dog.values()))

# Individual Items of Dictionary
print(dog.items())
print(list(dog.items()))

# length of dictionary
print(len(dog))

# Add item to dictionary
dog["favorite_food"] = "Meat"

# Remove item from dictionary
del dog["color"]
print(dog)

# Copy dictionary
dogCopy = dog.copy()

print(dogCopy)
