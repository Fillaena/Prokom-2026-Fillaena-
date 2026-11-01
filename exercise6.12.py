cities = {
    'edinburgh': {
        'country': 'Scotland',
        'population': 510000,
        'fact': 'it is the capital of Scotland and hosts the famous Edinburgh Fringe festival.',
        'landmarks': ['Edinburgh Castle', 'Arthur\'s Seat'],
    },
    'paris': {
        'country': 'France',
        'population': 2100000,
        'fact': 'it is home to the Eiffel Tower.',
        'landmarks': ['Eiffel Tower', 'Louvre Museum', 'Notre-Dame'],
    },
    'tokyo': {
        'country': 'Japan',
        'population': 14000000,
        'fact': 'it hosted the Olympics in 1964 and 2020.',
        'landmarks': ['Tokyo Tower', 'Senso-ji Temple'],
    },
}

for city, info in cities.items():
    print(city.upper())
    print(f"    Country    : {info['country']}")
    print(f"    Population : about {info['population']:,}")
    print(f"    Fact       : {info['fact']}")
    print(f"    Landmarks  : {', '.join(info['landmarks'])}\n")