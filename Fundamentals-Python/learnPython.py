# Functions
def hello(name="My Friend", age=18):
    print(f"Hello {name}, you are {str(age)} years old!")


hello("dat", 23)


def change(value):
    value["name"] = "dat"


val = {"name": "Beau"}
change(val)

print(val)


def hello(name):
    if not name:
        return
    print('Hello ' + name)


hello("Dat")
