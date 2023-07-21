# Break and continue
items = ["a", "b", "c", "d", "e"]
for item in items:
    if(item == "a"):
        continue
    print(item)
    
for item in items:
    if(item == "c"):
        break
    print(item)