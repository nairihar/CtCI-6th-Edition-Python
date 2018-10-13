def stringCompression(string):
  compression = ''
  character = None
  count = 0

  for c in string:
    if not character:
      character = c
      count += 1
    elif c == character:
      count += 1
    else:
      compression += character + str(count)
      character = c
      count = 1
    
  compression += character + str(count)
  
  return compression

print(stringCompression('aabbbaacczzz'))
