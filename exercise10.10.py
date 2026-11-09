from pathlib import Path

filenames = ['alice.txt', 'prideandprejudice.txt']

for filename in filenames:
    path = Path(__file__).parent / filename
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, file {filename} not found.")
    else:
        lowered = contents.lower()
        count_the = lowered.count('the')
        count_the_space = lowered.count('the ')
        print(f"{filename}: 'the' appears {count_the} times, 'the ' (with space) {count_the_space} times.")