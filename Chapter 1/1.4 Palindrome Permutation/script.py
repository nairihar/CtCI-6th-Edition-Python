def palindromePermutation(str):
  dict = {}
  single_count = 0
  for c in str:
    _c = c.lower()

    if _c == ' ':
      continue

    if _c in dict:
      dict[_c] += 1
      if dict[_c] == 2:
        single_count -= 1
    else:
      dict[_c] = 1
      single_count += 1

  if single_count > 1:
    return False

  return True


print(palindromePermutation('Tact Coa'))
print(palindromePermutation('This is not a Palindrome Permutation'))
