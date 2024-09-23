
hs = set()

# Add item into Set - O(1)

hs.add(1)
hs.add(2)
hs.add(3)
print(hs)

# Lookup if item in set - O(1)
if 5 not in hs:
  print(False)

if 1 in hs:
  print(True)

# Remove item from set - O(1)
hs.remove(3)

print(hs)

# Set construction - O(S) - S is the length of the string
string = 'aaaaaaabbbbbbbbbbbccccccccceeeeeeeee'
sett = set(string)

print(sett)

# Loop over items in set - O(n)
for x in hs:
  print(x)