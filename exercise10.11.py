from pathlib import Path
import json

number = int(input("What is your favorite number? "))

path = Path(__file__).parent / 'favorite_number.json'
contents = json.dumps(number)
path.write_text(contents)

from pathlib import Path
import json

path = Path(__file__).parent / 'favorite_number.json'
contents = path.read_text()
number = json.loads(contents)

print(f"I know your favorite number! It's {number}.")