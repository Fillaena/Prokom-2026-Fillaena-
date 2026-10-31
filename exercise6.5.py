rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'rhine': 'germany',
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRiver in the dictionary:")
for river in rivers.keys():
    print(river.title())

print("\nCountry in the xdictionary:")
for country in rivers.values():
    print(country.title())