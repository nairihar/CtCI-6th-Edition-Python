def is_substring(string, sub):
  return string.find(sub) != -1

def stringRotation(s1, s2):
  if len(s1) != len(s2):
    return False
  return is_substring((s1*2), s2)

print(stringRotation('waterbottle', 'erbottlewat'))
print(stringRotation('foo', 'foofoo'))
