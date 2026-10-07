n = input("Введіть ціле число: ")
if n.startswith("-"):
    print("-" + n[:0:-1])
else:
    print(n[::-1])