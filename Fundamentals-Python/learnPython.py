# Polymorphism 
class Flying:
    def fly(self):
        pass

class Airplane(Flying):
    def fly(self):
        print("Flying in an airplane.")

class Bird(Flying):
    def fly(self):
        print("Flying like a bird.")

def fly_high(flying_object):
    flying_object.fly()

fly_high(Airplane())
fly_high(Bird())
