favorite_languages = {
    'fillaena': 'python',
    'alfa': 'java',
    'putri': 'c++',
    'bipta': 'javascript',
}

people = ['fillaena', 'alfa', 'aulia', 'ael', 'putri', 'bipta']

for person in people:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for taking the poll.")
    else:
        print(f"{person.title()}, please take the poll!")