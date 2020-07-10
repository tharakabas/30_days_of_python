set1 = {'item1', 'item2', 'item3', 'item4'}
print(set1)

print(len(set1))

set1.add('item5')

print(set1)

set1.update(['item8', 'item6', 'item7'])
print(set1)

set1.remove('item2')
print(set1)

# Difference between two sets
set2 = {'item1', 'item2', 'item3', 'item4'}
print(set1.difference(set2))
print(set2.difference(set1))

