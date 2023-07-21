# Nested Functions
def count():
    count = 0

    def increment():
        nonlocal count  # Sử dụng nonlocal keyword để tham chiếu biến count trong scope bên ngoài increment()
        count += 1
        return count

    return increment


sum = count()

print(sum())
print(sum())
print(sum())


        