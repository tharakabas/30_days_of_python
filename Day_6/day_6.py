dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

print(dct)
print(len(dct))

print(dct['key1'])
print(dct.get('key1'))

# adding values
dct['key5'] = 'value5'
print(dct)

# edit items
dct['key1'] = 'new value'
