print('Example with SORTED function')

fruits = ['grape', 'raspberry', 'apple', 'banana']
sorted_fruits = sorted(fruits)
print('default sorted ', sorted_fruits)
sorted_fruits = sorted(fruits, reverse=True)
print('reverse sorted ', sorted_fruits)
sorted_fruits = sorted(fruits, key=len)
print('sorted with len items', sorted_fruits)
sorted_fruits = sorted(fruits, key=len, reverse=True)
print('sorted with len items in reverse way', sorted_fruits)

print('Examples with SORT function')

fruits = ['grape', 'raspberry', 'apple', 'banana']
print('sort is a inplace function will return None', fruits.sort())
print(fruits)