#file reader
from pathlib import Path

path = Path(__file__).parent / 'exercise10.3.txt'
contents = path.read_text()

for line in contents.splitlines():
    print(line)
    
#pi string
from pathlib import Path

path = Path(__file__).parent / 'exercise10.3.txt'
contents = path.read_text()

pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))

#pi million
from pathlib import Path

path = Path(__file__).parent / 'exercise10.3.txt'
contents = path.read_text()

pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))