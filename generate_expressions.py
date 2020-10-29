import array

symbols = "åß∂çåßœ"
print("Expressao geradora tuple", tuple(ord(symbol) for symbol in symbols))

print("Expressao geradora array", array.array("I", (ord(symbol) for symbol in symbols)))
