from pathlib import Path
import json

path = Path(__file__).parent / 'user_info.json'

if path.exists():
    contents = path.read_text()
    user = json.loads(contents)
else:
    user = {
        'name': input("What is your name? "),
        'age': input("How old are you? "),
        'color': input("What is your favorite color? "),
    }
    contents = json.dumps(user)
    path.write_text(contents)
    print("Thanks, I'll remember that!")

print("\nHere is what I remember about you:")
print(f"Name: {user['name']}")
print(f"Age: {user['age']}")
print(f"Favorite color: {user['color']}")