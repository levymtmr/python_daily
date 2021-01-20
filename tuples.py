# Tuplas como registros.
lax_coodinates = (33.9425, -118.408056)
city, year, pop, chg, area = ("Tokyo", 2003, 32450, 0.66, 8014)
traveler_ids = [("USA", "31195855"), ("BRA", "CE342567")]
for passport in sorted(traveler_ids):
    print("%s/%s" % passport)

for country, _ in traveler_ids:
    print(country)

# Atribuir itens de um interável a uma tupla de variáveis.
lax_coodinates = (33.9425, -119.408056)
latitude, longitude = lax_coodinates  # desempacotamento de tupla
print("Latitude ->", latitude)
print("Longitude ->", longitude)

# Trocar o valores de duas variáveis sem usar variável temporária
a = "A"
b = "B"
a, b = b, a
print("a -> ", a)
print("b -> ", b)

# Prefixar um argumento com um * ao chamar uma função
print("Divmod ->", divmod(20, 8))
t = (20, 8)
print(divmod(*t))
quotient, remainder = divmod(*t)
print(quotient, remainder)

# Atribuições paralelas
a, b, *rest = range(5)
print(a, b, rest)
a, b, *rest = range(3)
print(a, b, rest)
a, b, *rest = range(2)
print(a, b, rest)
a, *b, c = range(5)
print(a, b, c)
