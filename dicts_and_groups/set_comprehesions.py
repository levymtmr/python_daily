from unicodedata import name

test = {chr(i) for i in range(32, 256) if "SIGN" in name(chr(i), "")}
print(test)
