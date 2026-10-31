pet_1 = {'animal': 'kucing', 'owner': 'Fillaena'}
pet_2 = {'animal': 'hamster', 'owner': 'Cava'}
pet_3 = {'animal': 'kelinci', 'owner': 'Alfa'}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"Hewan: {pet['animal']}")
    print(f"Pemilik: {pet['owner']}\n")