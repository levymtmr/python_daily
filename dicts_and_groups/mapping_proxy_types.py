from types import MappingProxyType

d = {1: "A"}
d_proxy = MappingProxyType(d)  # mapping view
print(d_proxy)
print(d_proxy[1])
try:
    d_proxy[2] = "x"
    print(d_proxy[2])
except TypeError:
    d[2] = "B"
    print(d_proxy)
    print(d_proxy[2])
