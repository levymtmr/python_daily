import sys
import re
import collections

"""
When you try get a key nonexistent
the defauldict will return a empty list
"""

WORD_RE = re.compile("\w+")

index = collections.defaultdict(list)

with open(sys.argv[1], encoding="utf-8") as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            colunm_no = match.start() + 1
            location = (line_no, colunm_no)
            index[word].append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])

print()
print("Missing keys to convert in str Class")


class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


"""
Convert the key for string if
the key didn't find.
"""
d = StrKeyDict0([("2", "two"), ("4", "four")])
print(d["2"])
print(d[4])
print(d.get("2"))
print(d.get(4))
print(d.get(1, "N/A"))
print(2 in d)
print(1 in d)

print(d[1])
