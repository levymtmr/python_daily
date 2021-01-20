lista = list(range(10))
print(lista)
lista[2:5] = [20, 30]
print(lista[2:5])
print(lista)
del lista[5:7]
print(lista)
lista[3::2] = [11, 22]
print(lista)
try:
    # needs to use a iterable object
    lista[2:5] = 100
    print(lista)
except Exception as e:
    print(e)
    lista[2:5] = [100]
    print(lista)
