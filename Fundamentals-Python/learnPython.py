# Classes
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print("Woof!")

# Tạo một đối tượng Dog và gọi phương thức speak
my_dog = Dog("Max", "Labrador")
my_dog.speak()  # In ra "Woof!"

# Truy cập thuộc tính từ lớp cha
print(my_dog.name)  # In ra "Max"  