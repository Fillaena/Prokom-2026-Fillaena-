# parameter population wajib (tes gagal)
def get_city_country(city, country, population):
    """Return a string like 'New York, Prague - population 5000000'."""
    return f"{city}, {country} - population {population}".title()

# population opsional 
def get_city_country(city, country, population=''):
    """Return a string like 'New York, Prague' or with population."""
    output = f"{city}, {country}"
    if population:
        output += f" - population {population}"
    return output.title()