from pathlib import Path

path = Path(__file__).parent / 'exercise10.1.txt'

contents = path.read_text()
print(contents)

lines = contents.splitlines()
for line in lines:
    print(line)