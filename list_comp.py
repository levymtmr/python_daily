# exemplo simples de list comp
symbols = "£¢¡™£¢∞"
codes = [ord(symbol) for symbol in symbols]
print(codes)


# A variais são de escolo locais
# Porém variaveis fora do escopo podem ser referenciadas

x = "ABC"
dummy = [ord(letter) for letter in x]
print("x ->", x)
print("dummy ->", dummy)


# Use listcomp em vez de map/filter
symbols = "£¢¡™£¢∞"
beyond_ascii = [ord(symbol) for symbol in symbols if ord(symbol) > 127]
print("Usando listcomp como map/filter", beyond_ascii)

# Usando map/filter para fazer rotinas em listas
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print("Usando map/filter direto", beyond_ascii)

# Produto cartesiano usando listcomp
colors = ["black", "white"]
sizes = ["S", "M", "L"]
tshirts = [(color, size) for color in colors for size in sizes]
print("Produto cartesiano usando listcompo", tshirts)
