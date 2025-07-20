file = input("Dateiname: ")

text = open(file, "r")
figures = int(text.readline())
books = int(text.readline())
shelf = []

for _ in range(books):
    shelf.append(int(text.readline()))

shelf.sort()
curmin = shelf[0]

for book in shelf:
    if book - curmin > 30:
        curmin = book
        figures -= 1

if figures < 0:
    print("Geht nicht")
else:
    print("Geht")