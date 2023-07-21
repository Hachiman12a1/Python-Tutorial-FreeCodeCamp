# loops

# While
count = 0
while count < 10:
    count += 1
    print(count)
    
print("Ended Loop")

# For
items = ["a", "b", "c", "d", "e"]
for item in items:
    print(item)
    
for item in range(15):
    print(item)
    
for index,item in enumerate(items):
    print(index,item)