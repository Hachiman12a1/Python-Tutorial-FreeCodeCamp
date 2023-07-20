dogs = ['Roger', 1, "Syd", True, "Quincy", 7]

# Access List item index
dogs[2] = "Beau"
print("Beau" in dogs)

# Slice Item
print(dogs[2:5])
print(dogs[:3])

# Length of list
print(len(dogs))

# Add item
dogs.append("dat")
dogs.extend(["world", "Cloud"])
dogs += ["world1", "Cloud1"]

# Remove Item
dogs.remove("Quincy")
# Remove Last Item
dogs.pop()
print(dogs)

# Insert Item According To Index
print("----List Items--------")
items = ['Roger', 1, "Syd", True, "Quincy", 7]

items.insert(2, "dat")
items[1:2] = ["abc", "def"]

print(items)
