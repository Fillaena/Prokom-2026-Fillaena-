cities = ['Seoul', 'London', 'San Fransisco']
print(cities)

cities.append('Melbourne')
print(cities)

cities.insert(1, 'Edinburgh')
print(cities)

popped = cities.pop()
print(f"{popped} dihapus dengan pop(): {cities}")

cities.remove('San Fransisco')
print(cities)

cities.append('Prague')

del cities[0]
print(cities)

print(f"Jumlah kota: {len(cities)}")

print(f"Kota terakhir: {cities[-1]}")

print(sorted(cities))
print(cities)

cities.reverse()
print(cities)

cities.sort()
print(cities)

cities.sort(reverse=True)
print(cities)