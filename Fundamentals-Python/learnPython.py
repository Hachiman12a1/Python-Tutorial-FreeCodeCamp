# Sets
set1 = {"Roger", "Syd"}
set2 = {"Roger", "Beau"}

mixSetAnd = set1 & set2
mixSetOr = set1 | set2
mixSetSubtract = set1 - set2
compareSet = set1 > set2

print(mixSetAnd, mixSetOr, mixSetSubtract, compareSet, list(mixSetOr))
