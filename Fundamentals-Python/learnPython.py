# Variable Scope
def test():
    age = 8
    print(age)


print(age)  # Error Because of variable scope problem
test()
