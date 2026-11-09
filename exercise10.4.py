from pathlib import Path

name = input("What's your name? ")

path = Path(__file__).parent / 'guest.txt'
path.write_text(name)