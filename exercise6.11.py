cities = {
    'edinburgh': {
        'country': 'Scotland',
        'population': 510000,
        'fact': 'it is the capital of Scotland and hosts the famous Edinburgh Fringe festival.',
    },
    'paris': {
        'country': 'France',
        'population': 2100000,
        'fact': 'it is home to the Eiffel Tower.',
    },
    'tokyo': {
        'country': 'Japan',
        'population': 14000000,
        'fact': 'it is the capital of Japan.',
    },
}

for city, info in cities.items():
    print(f"City: {city.title()}")
    print(f"    Country: {info['country']}")
    print(f"    Population: about {info['population']:,}")
    print(f"    Fact: {info['fact']}\n")