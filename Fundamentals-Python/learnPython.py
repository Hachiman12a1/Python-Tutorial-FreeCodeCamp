# Exceptions
try:
    result = 2 /0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    result = 1
    
print(result)

try:
    raise Exception("An error!")
except Exception as error:
    print(error)


class DogNotFoundException(Exception):
    print("inside!")
    pass

try:
    raise DogNotFoundException("An error!")
except DogNotFoundException:
    print("Dog not found!")