def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return f"{city.title()}, {country.title()}"


print(city_country('santiago', 'chile'))
print(city_country('prague', 'czech republic'))
print(city_country('edinburgh', 'scotland'))