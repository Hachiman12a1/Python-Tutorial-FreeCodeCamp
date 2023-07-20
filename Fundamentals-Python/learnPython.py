done = False or ""
print(done)
print(type(done) == bool)
print("yes") if done else print("no")


book_1_read = "hi"
book_2_read = False

read_any_book = any([book_1_read, book_2_read])
read_all_book = all([book_1_read, book_2_read])
print(read_any_book)
print(read_all_book)
