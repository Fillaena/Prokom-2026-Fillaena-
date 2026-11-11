from exercise11_1_functions import get_city_country


def test_city_country():
    formatted = get_city_country('new york', 'prague')
    assert formatted == 'New York, Prague'