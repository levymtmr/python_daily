## The wrong way to get default values in a dict

import sys
import re

WORD_RE = re.compile('\w+')
index = {}

with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # Not pythonic way
            # occurrences = index.get(word, [])
            # occurrences.append(location)
            # index[word] = occurrences
            # pythonic way
            index.setdefault(word, []).append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])