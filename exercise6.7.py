person_1 = {
    'first_name': 'Fillaena',
    'last_name': 'Bipta',
    'age': 18,
    'city': 'Purwokerto',
}

person_2 = {
    'first_name': 'Alfa',
    'last_name': 'Nurochman',
    'age': 28,
    'city': 'Purwokerto',
}

person_3 = {
    'first_name': 'Maekky',
    'last_name': 'Cava',
    'age': 14,
    'city': 'Purwokerto',
}

people = [person_1, person_2, person_3]

for person in people:
    print(f"Nama: {person['first_name']} {person['last_name']}")
    print(f"Umur: {person['age']}")
    print(f"Kota: {person['city']}\n")