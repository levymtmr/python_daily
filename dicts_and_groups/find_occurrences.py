needles = [1, 3, 6, 9]
haystack = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 3, 6, 9]
# found = len(set(needles) & set(haystack))
found = len(set(needles).intersection(haystack))
print(found)

found_2 = 0
for n in needles:
    if n in haystack:
        found_2 += 1

print(found_2)
