#  Map, Filter, Reduce
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6]
expenses = [("Dinner" , 80), ("Breakfast" , 120)]

def double(a):
    return a*2

def filterDivision(a):
    if(a %2 == 0):
        return a
    
def expenseSum(a,b) :
    return a[1] + b[1]

mapResult = list(map(double, numbers))
filterResult = list(filter(filterDivision, numbers))
reduceResult = reduce(expenseSum, expenses)


print(mapResult)
print(filterResult)
print(reduceResult)