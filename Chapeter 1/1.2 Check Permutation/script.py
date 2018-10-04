# using O(N) solution which uses some space

def checkPermutation(str1, str2):
  str2_len = len(str2)
  if len(str1) != str2_len:
    return False

  for i1, c1 in enumerate(str1):
    i2_last = str2_len - i1 - 1
    if c1 != str2[i2_last]:
      return False
  
  return True


print(checkPermutation('test', 'test'))
print(checkPermutation('abc', 'cba'))