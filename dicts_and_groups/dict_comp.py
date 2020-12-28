DIAL_CODE = [
    (1, 'Brasil'),
    (2, 'Australia'),
    (3, 'China'),
    (4, 'Franca'),
    (5, 'Belgica')
]

country_code = {country: code for code, country in DIAL_CODE}
print('All countries ->', country_code)

country_code_uppercase = {code: country.upper() for country, code in country_code.items() if code < 4}
print(country_code_uppercase)

test_country = {code: country for country, code in country_code.items()}
print('calling', test_country)