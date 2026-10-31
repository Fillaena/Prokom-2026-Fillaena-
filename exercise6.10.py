favorite_numbers = {
    'Fillaena': [2, 11],
    'Alfa': [12, 28],
    'Cava': [12],
    'Putri': [8, 20, 100],
    'Bipta': [110],
}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"    {number}")
    print()