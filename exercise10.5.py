from pathlib import Path

names = []

while True:
    name = input("Input your name (ketik 'q' untuk selesai): ")
    if name == 'q':
        break
    names.append(name)

contents = ""
for name in names:
    contents += f"{name}\n"

path = Path(__file__).parent / 'guest_book.txt'
path.write_text(contents)