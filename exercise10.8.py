from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    path = Path(__file__).parent / filename
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"Sorry, file {filename} not found.")
    else:
        print(f"Isi {filename}:")
        print(contents)