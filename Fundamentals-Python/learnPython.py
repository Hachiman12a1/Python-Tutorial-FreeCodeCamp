# Nested Functions
def count():
    count = 0

    def increment():
        nonlocal count  # Sử dụng nonlocal keyword để tham chiếu biến count trong scope bên ngoài increment()
        count += 1
        print(count)

    increment()


count()


def talk(phrase) :
    def say(word) :
        print(word)
        
    words = phrase.split(" ")
    for word in words:
        say(word)
        
talk("My name is Dat")
        