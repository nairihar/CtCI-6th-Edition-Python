def urlify(str):
  url = ''
  space_count = 0

  for c in str:
    if c == ' ':
      space_count += 1
    elif space_count > 0:
      url += '%20' * space_count
      space_count = 0
    else:
      url += c
  
  return url

print(urlify('Mr John'))
print(urlify('Mr Jo  hn'))
print(urlify('Mr John    '))