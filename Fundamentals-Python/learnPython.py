# Decorators

def logTime(func):
    def wrapper():
        print("before")
        val = func()
        print("after")
        return val
    
    return wrapper  

@logTime
def hello():
    print("hello")
    
hello()