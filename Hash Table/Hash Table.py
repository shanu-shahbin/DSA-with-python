
ht = {'shane': 1, 'watson': 2, 'smith': 3}

# Add key:val in dictionary: O(1)

ht['head'] = 4
print(ht)

# Check for presence of key in dictionary: O(1)
if 'head' in ht:
  print(True)

# Check the value corresponding to a key in the dictionary: O(1)
print(ht['shane'])

# Loop over the key:val pairs of the dictionary: O(n)
for key, val in ht.items():
  print(f'key {key}: val {val}')
