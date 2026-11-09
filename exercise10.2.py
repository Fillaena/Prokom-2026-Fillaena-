from pathlib import Path

path = Path(__file__).parent / 'exercise10.1.txt'
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line.replace('Python', 'C'))