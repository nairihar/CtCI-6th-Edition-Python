# Solution using loops

def isUniqueByLoops(str):
  for i, c in enumerate(str):
    for j in range(i + 1, len(str)):
      if c == str[j]:
        return False
  return True

print(isUniqueByLoops('test'))
print(isUniqueByLoops('cola'))


# Solution using array of booleans
# https://www.programiz.com/python-programming/methods/built-in/ord

def isUniqueByBoolArray(str):
  char_set = [False] * 128
  for c in str:
    i = ord(c)

    if char_set[i]:
      return False

    char_set[i] = True

  return True

print(isUniqueByBoolArray('test'))
print(isUniqueByBoolArray('cola'))
