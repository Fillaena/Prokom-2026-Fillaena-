foods = ('nasi putih', 'ayam goreng', 'tempe', 'sayur asem', 'sambal')

print("Menu buffet:")
for food in foods:
    print(food)

# foods[0] = 'nasi goreng'   # TypeError: tuple tidak bisa diubah

foods = ('nasi putih', 'ayam goreng', 'tahu', 'sayur asem', 'es teh')

print("\nMenu buffet yang baru:")
for food in foods:
    print(food)