def oneAway(str, changed_str):
  r = False
  d = False
  a = False

  changed = False

  diff = len(changed_str) - len(str)

  if diff == 0: # replace
    r = True
    for i, c in enumerate(str):
      if c != changed_str[i]:
        if changed:
          return False
        changed = True

  elif diff == 1: # added
    a = True
    j = 0

    for i, c_c in enumerate(changed_str):
      if len(str) == i and not changed:
        return True

      if str[i - j] != c_c:
        if changed:
          return False
        changed = True
        j = 1
    
    return True

  elif diff == -1: # removed
    d = True
    j = 0

    for i, c in enumerate(str):
      if len(str) == i + 1 and not changed:
        return True

      if c != changed_str[i - j]:
        if changed:
          return False
        changed = True
        j = 1

  else:
    return False

  return changed


print(oneAway('pale', 'ple'))
print(oneAway('pales', 'pale'))
print(oneAway('pale', 'ale'))
print(oneAway('pale', 'ake'))
print(oneAway('pale', 'pll'))

print(oneAway('pale', 'pales'))
print(oneAway('pale', 'palds'))
print(oneAway('pale', 'mkale'))

print(oneAway('pale', 'bale'))

print(oneAway('pale', 'bake'))
