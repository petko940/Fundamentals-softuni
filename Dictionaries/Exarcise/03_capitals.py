country_names = [x for x in input().split(", ")]
capital_cities = [x for x in input().split(", ")]

[print(f"{country} -> {capital}") for country, capital in zip(country_names, capital_cities)]
