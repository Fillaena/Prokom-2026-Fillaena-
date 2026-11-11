from exercise11_2_functions import get_city_country


def test_city_country():
    """Does a string like 'Santiago, Chile' work?"""
    formatted = get_city_country('santiago', 'chile')
    assert formatted == 'Santiago, Chile'


def test_city_country_population():
    """Does a string like 'Santiago, Chile - Population 5000000' work?"""
    formatted = get_city_country('santiago', 'chile', population=5000000)
    assert formatted == 'Santiago, Chile - Population 5000000'