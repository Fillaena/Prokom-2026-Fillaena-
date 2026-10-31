favorite_places = {
    'Fillaena': ['London Bridge', 'Lake Como'],
    'Alfa': ['Karimunjawa'],
    'Aelen': ['Ranukumbolo', 'Lombok', 'Labuan Bajo'],
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"    {place}")
    print()