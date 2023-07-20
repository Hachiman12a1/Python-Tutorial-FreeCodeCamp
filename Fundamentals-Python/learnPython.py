items = ['Roger', "dat", "Syd", "Bz", "Quincy", "beau"]

# Copy List
itemsCopy = items[:]

# Sort
# Method 1
# items.sort(key=str.lower)

# Method 2 - Not modifying original lists
itemsSort = sorted(items, key=str.lower)
print(items)
print(itemsSort)
print(itemsCopy)
